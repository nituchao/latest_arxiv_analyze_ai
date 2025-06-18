import requests
import json

def load_paper_jsonl(file_path):
    papers = []
    with open(file_path, "r", encoding="utf-8") as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            papers.append(data)

    return papers

def translate_paper(paper):
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    post_header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 23fbfd7c-a69f-465c-8f9a-ed94956fd8b9"
    }
    post_body = {
        "model": "deepseek-r1-250120",
        "messages": [
            {"role": "system","content": "你是人工智能助手."},
            {"role": "user","content": f"请把下面的英文论文摘要翻译成中文'{paper['abstract']}'"}
        ]
    }

    try:
        response = requests.post(url, headers=post_header, json=post_body)
        result = response.json()
        print(result)
        print(result['choices'][0]['message']['content'])
        paper["abstract_zh"] = result['choices'][0]['message']['content']
    except Exception as e:
        print(e)
        paper["abstract_zh"] = ""

def translate_papers(papers):
    for paper in papers:
        paper = translate_paper(paper)
        print(paper)

        break

if __name__ == "__main__":
    file_path = "/Users/bytedance/Documents/Workspace/codes_nituchao/nituchao_arxiv/arxiv_papers/arxiv_papers.jsonl"
    papers = load_paper_jsonl(file_path=file_path)
    translate_papers(papers=papers)