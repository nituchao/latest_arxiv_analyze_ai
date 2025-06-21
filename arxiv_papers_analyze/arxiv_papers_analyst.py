from arxiv_papers_utils import init_environment_conf
from pydantic import BaseModel, Field
from datetime import datetime
from openai import OpenAI
import json
import time
import os

class ArxivPaperAnalyst:
    """
    Arxiv Paper Analyst
    Step2: analyze the arxiv paper by llm
    """
    def __init__(self, arxiv_papers_crawled_jsonl, llm_api_key, llm_base_url, llm_model_name, arxiv_analysis_language, prompt_system, prompt_user, arxiv_papers_analyzed_jsonl):
        self.llm_api_key = llm_api_key
        self.llm_base_url = llm_base_url
        self.llm_model_name = llm_model_name

        self.prompt_user = prompt_user
        self.prompt_system = prompt_system

        self.current_date = datetime.now().strftime("%Y%m%d")
        self.arxiv_analysis_language = arxiv_analysis_language
        self.arxiv_papers_crawled_jsonl = arxiv_papers_crawled_jsonl.format(self.current_date)
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl.format(self.current_date)

    def load_arxiv_paper_jsonl(self, filename):
        papers = []

        with open(self.arxiv_papers_crawled_jsonl, "r", encoding="utf-8") as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                papers.append(data)

        return papers

    def analyze_arxiv_paper_by_llm(self, paper):
        paper_analysis = {}
        paper_analysis['title_en'] = paper['title']
        paper_analysis['authors'] = paper['authors']
        paper_analysis['pdf_url'] = paper['pdf_url']
        paper_analysis['html_url'] = paper['html_url']

        try:
            client = OpenAI(api_key=self.llm_api_key, base_url=self.llm_base_url)
        
            completion = client.beta.chat.completions.parse(
                model=self.llm_model_name,
                messages=[
                    {"role": "system", "content": self.prompt_system.format(self.arxiv_analysis_language)},
                    {"role": "user", "content": self.prompt_user.format(paper['abstract'], paper['title'])},
                ],
                response_format={"type": "json_object"}
            )
            
            paperAnalysis = completion.choices[0].message.content
            paperAnalysis = json.loads(paperAnalysis)
            
            paper_analysis['title'] = paperAnalysis['title']
            paper_analysis['background'] = paperAnalysis['background']
            paper_analysis['innovation'] = paperAnalysis['innovation']
            paper_analysis['conclusion'] = paperAnalysis['conclusion']
        except Exception as e:
            paper_analysis['title'] = ""
            paper_analysis['abstract'] = ""
            paper_analysis['innovation'] = ""
            paper_analysis['conclusion'] = ""
            print(f"error happens when analyze paper {paper['title']}, error message: {e}")

        return paper_analysis

    def analyze_arxiv_full_paper_list_by_llm(self, origin_paper_list):
        idx = 0
        total_count = len(origin_paper_list)

        analyzed_paper_list = []
        for origin_paper in origin_paper_list:
            analyzed_paper = self.analyze_arxiv_paper_by_llm(origin_paper)
            analyzed_paper_list.append(analyzed_paper)
            
            print(f"analyze paper {idx+1}/{total_count}, title: {analyzed_paper['title']}")
            time.sleep(1)
            idx = idx + 1

            if idx >= 10:
                break

        return analyzed_paper_list

    def save_arxiv_full_paper_list_to_jsonl(self, analyzed_paper_list):

        full_papers_count = 0
        with open(self.arxiv_papers_analyzed_jsonl, "w", encoding="utf-8") as jsonl_file:
            for paper in analyzed_paper_list:
                json.dump(paper, jsonl_file, ensure_ascii=False)
                jsonl_file.write("\n")
                full_papers_count += 1

        return full_papers_count

    def process_arxiv_papers_analyze(self):
        origin_paper_list = self.load_arxiv_paper_jsonl(self.arxiv_papers_crawled_jsonl)
        analyzed_paper_list = self.analyze_arxiv_full_paper_list_by_llm(origin_paper_list)
        full_papers_count = self.save_arxiv_full_paper_list_to_jsonl(analyzed_paper_list)

        return full_papers_count
    
if __name__ == '__main__':
    conf = init_environment_conf()

    llm_api_key = conf['llm']['api_key'] if conf['llm']['api_key'].strip() else os.environ.get('LLM_API_KEY', '').strip()
    llm_base_url = conf['llm']['base_url'] if conf['llm']['base_url'].strip() else os.environ.get('LLM_BASE_URL', '').strip()
    llm_model_name = conf['llm']['model_name'] if conf['llm']['model_name'].strip() else os.environ.get('LLM_MODEL_NAME', '').strip()

    prompt_user = conf['prompt']['user']
    prompt_system = conf['prompt']['system']

    arxiv_analysis_language = conf['analysis']['arxiv_analysis_language']
    arxiv_papers_crawled_jsonl = conf['analysis']['arxiv_papers_crawled_jsonl']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']

    print(f"llm_api_key: {llm_api_key}, llm_base_url: {llm_base_url}, llm_model_name: {llm_model_name}")

    arxiv_papers_analyst = ArxivPaperAnalyst(arxiv_papers_crawled_jsonl, llm_api_key, llm_base_url, llm_model_name, arxiv_analysis_language, prompt_system, prompt_user, arxiv_papers_analyzed_jsonl)
    arxiv_papers_analyzed_count = arxiv_papers_analyst.process_arxiv_papers_analyze()

    print(f"Arxiv Papers Analyze Done! analyze {arxiv_papers_analyzed_count} arxiv papers")