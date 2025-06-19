from pydantic import BaseModel, Field
from openai import OpenAI
from tqdm import tqdm
import requests
import json
import time

class PaperAnalysis(BaseModel):
    abstract: str=Field(description='describe the abstract of this paper')
    innovation: str=Field(description='describe the innovation of this paper')
    conclusion: str=Field(description='describe the conclusion of this paper')

def load_paper_jsonl(file_path):
    papers = []
    with open(file_path, "r", encoding="utf-8") as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            papers.append(data)

    return papers

def analyze_paper_by_llm_client(paper):
    client = OpenAI(api_key="23fbfd7c-a69f-465c-8f9a-ed94956fd8b9", 
                    base_url="https://ark.cn-beijing.volces.com/api/v3")
    
    completion = client.beta.chat.completions.parse(
        model="ep-20250619215522-gztbk",
        messages=[
            {"role": "system", "content": "You are a professional paper analyst.You should not respond too long output.Your output should in Chinese."},
            {"role": "user", "content": f"Please analyze the following abstract of papers. Content: {paper['abstract']}"},
        ],
        response_format=PaperAnalysis,
        extra_body={
            "thinking": {
                "type": "disabled" # 不使用深度思考能力
            }}
    )

    paper_analysis = {}
    paper_analysis['title'] = paper['title']
    paper_analysis['authors'] = paper['authors']
    paper_analysis['pdf_url'] = paper['pdf_url']
    paper_analysis['html_url'] = paper['html_url']

    try:
        paperAnalysis = completion.choices[0].message.parsed
        
        paper_analysis['abstract'] = paperAnalysis.abstract
        paper_analysis['innovation'] = paperAnalysis.innovation
        paper_analysis['conclusion'] = paperAnalysis.conclusion
    except Exception as e:
        print(f"分析失败：{e}")
        paper_analysis['abstract'] = ""
        paper_analysis['innovation'] = ""
        paper_analysis['conclusion'] = ""

    return paper_analysis


def analyze_paper_by_llm(paper):
    paper_analysis = {}
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    post_header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 23fbfd7c-a69f-465c-8f9a-ed94956fd8b9"
    }
    post_body = {
        "model": "ep-20250619200738-6dl76",
        "messages": [
            {"role": "system","content": "您是一名专业的论文分析师。请严格按照要求输出JSON格式的分析结果，仅包含'abstract'、'innovation'、'conclusion'三个字段，无其他内容。请使用简体中文输出。"},
            {"role": "user","content": f"请分析下面的论文摘要，输出包含这三个字段的JSON：'{paper['abstract']}'"}
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "joke_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "abstract": {
                            "type": "string"
                        },
                        "innovation": {
                            "type": "string"
                        },
                        "conclusion": {
                            "type": "string"
                        }
                    }
                },
                "required": ["abstract", "innovation", "conclusion"]
            }
        }
    }

    paper_analysis['title'] = paper['title']
    paper_analysis['authors'] = paper['authors']
    paper_analysis['pdf_url'] = paper['pdf_url']
    paper_analysis['html_url'] = paper['html_url']

    try:
        response = requests.post(url, headers=post_header, json=post_body)
        result = response.json()
        analysis_content = result['choices'][0]['message']['content']
        analysis_json = json.loads(analysis_content)  # 解析JSON
        # 修改3：将三个字段存入结果
        paper_analysis['摘要'] = analysis_json.get('摘要', '')
        paper_analysis['创新点'] = analysis_json.get('创新点', '')
        paper_analysis['关键结论'] = analysis_json.get('关键结论', '')
    except Exception as e:
        print(f"分析失败：{e}")
        paper_analysis['摘要'] = ""
        paper_analysis['创新点'] = ""
        paper_analysis['关键结论'] = ""

    return paper_analysis

def analyze_papers(origin_paper_list):
    analyzed_paper_list = []
    idx = 0
    for origin_paper in tqdm(origin_paper_list):
        analyzed_paper = analyze_paper_by_llm_client(origin_paper)
        analyzed_paper_list.append(analyzed_paper)
        idx += 1

        if idx >= 10:
            break

    return analyzed_paper_list

def save_papers_to_jsonl(analyzed_paper_list, file_path):
    with open("arxiv_papers_analyzed.jsonl", "w", encoding="utf-8") as jsonl_file:
        for paper in analyzed_paper_list:
            json.dump(paper, jsonl_file, ensure_ascii=False)
            jsonl_file.write("\n")

if __name__ == "__main__":
    file_path = "/Users/bytedance/Documents/Workspace/codes_nituchao/nituchao_arxiv/arxiv_papers/arxiv_papers.jsonl"
    origin_paper_list = load_paper_jsonl(file_path=file_path)
    analyzed_paper_list = analyze_papers(origin_paper_list=origin_paper_list)
    save_papers_to_jsonl(analyzed_paper_list, file_path="arxiv_papers_analyzed.jsonl")