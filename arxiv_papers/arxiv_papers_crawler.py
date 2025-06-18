import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

def crawl_arxiv_cs_papers():
    base_url = "https://arxiv.org"
    target_url = f"{base_url}/list/cs.AI/new"

    # 设置请求头模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # 获取页面内容
    response = requests.get(target_url, headers=headers)

    # 检查请求是否成功
    response.raise_for_status() 

    # 解析HTML
    soup = BeautifulSoup(response.text, 'lxml')

    # 定位所有论文条目（arXiv页面使用dl>dt+dd结构组织论文）
    papers = []
    for dt, dd in zip(soup.select("dl > dt"), soup.select("dl > dd")):
        # 提取链接（dt标签包含链接信息）
        links = dt.find_all("a")
        html_link = urljoin(base_url, dt.find_all(title="Abstract")[0]["href"])
        pdf_link = urljoin(base_url, dt.find_all(title="Download PDF")[0]["href"])

        # 提取标题（dd标签中的.title类）
        title = dd.find("div", class_="list-title").get_text(strip=True).replace("Title:", "")

        # 提取作者信息（dd标签中的.authors类）
        authors = dd.find("div", class_="list-authors").get_text(strip=True)

        # 提取摘要（dd标签中的.abstract类）
        abstract = dd.find("p", class_="mathjax").get_text(strip=True)

        papers.append({
            "pdf_url": pdf_link,
            "html_url": html_link,
            "authors": authors,
            "title": title,
            "abstract": abstract
        })

    # 保存为jsonl格式（每行一个JSON对象）
    with open("arxiv_papers.jsonl", "w", encoding="utf-8") as jsonl_file:
        for paper in papers:
            json.dump(paper, jsonl_file, ensure_ascii=False)
            jsonl_file.write("\n")

if __name__ == "__main__":
    crawl_arxiv_cs_papers()
    print("Done, Saved to arxiv_papers.jsonl")