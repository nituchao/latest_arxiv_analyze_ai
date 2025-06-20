from pydantic import BaseModel, Field
from datetime import datetime
from openai import OpenAI
import requests
import json
import time

class PaperAnalysis(BaseModel):
    title: str=Field(description='translate the title of this paper')
    abstract: str=Field(description='describe the abstract of this paper')
    innovation: str=Field(description='describe the innovation of this paper')
    conclusion: str=Field(description='describe the conclusion of this paper')

class ArxivPaperAnalyst:
    """
    Arxiv Paper Analyst
    """
    def __init__(self, filename, llm_api_key, llm_base_url, llm_model_name, arxiv_analysis_language, prompt_system, prompt_user, arxiv_papers_analyzed_jsonl):
        self.filename = filename
        self.llm_api_key = llm_api_key
        self.llm_base_url = llm_base_url
        self.llm_model_name = llm_model_name

        self.prompt_user = prompt_user
        self.prompt_system = prompt_system

        self.arxiv_analysis_language = arxiv_analysis_language
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl

    def load_arxiv_paper_jsonl(self, filename):
        papers = []
        with open(filename, "r", encoding="utf-8") as jsonl_file:
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
                response_format=PaperAnalysis,
                extra_body={
                    "thinking": {
                        "type": "disabled"
                    }}
            )
            
            paperAnalysis = completion.choices[0].message.parsed
            
            paper_analysis['title'] = paperAnalysis.title
            paper_analysis['abstract'] = paperAnalysis.abstract
            paper_analysis['innovation'] = paperAnalysis.innovation
            paper_analysis['conclusion'] = paperAnalysis.conclusion
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
            
            print(f"analyze paper {idx}/{total_count}, title: {analyzed_paper['title']}")
            time.sleep(1)

        return analyzed_paper_list

    def save_arxiv_full_paper_list_to_jsonl(self, analyzed_paper_list):
        current_date = datetime.now().strftime("%Y%m%d")
        arxiv_papers_analyzed_jsonl = self.arxiv_papers_analyzed_jsonl.format(current_date)

        with open(arxiv_papers_analyzed_jsonl, "w", encoding="utf-8") as jsonl_file:
            for paper in analyzed_paper_list:
                json.dump(paper, jsonl_file, ensure_ascii=False)
                jsonl_file.write("\n")