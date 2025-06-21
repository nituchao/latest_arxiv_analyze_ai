import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
from arxiv_papers_utils import init_environment_conf

class ArxivPapersCrawler:
    """
    Arxiv Papers Crawler
    Step1: crawl arxiv papers by topic list
    """
    def __init__(self, arxiv_base_url, arxiv_topic_url, arxiv_topic_list, arxiv_papers_crawled_jsonl):
        self.arxiv_base_url = arxiv_base_url
        self.arxiv_topic_url = arxiv_topic_url
        self.arxiv_topic_list = arxiv_topic_list
        self.arxiv_papers_crawled_jsonl = arxiv_papers_crawled_jsonl

    def crawl_arxiv_papers_by_single_topic(self, topic):
        # set request header to simulate browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # get page content
        request_url = self.arxiv_topic_url.format(topic)
        response = requests.get(request_url, headers=headers)

        # check if the request was successful
        response.raise_for_status() 

        # parse html content
        soup = BeautifulSoup(response.text, 'lxml')

        # find all paper entries (arxiv page uses dl>dt+dd structure to organize papers)
        papers = []
        for dt, dd in zip(soup.select("dl > dt"), soup.select("dl > dd")):
            # extract links (dt tags contain link information)
            links = dt.find_all("a")
            html_link = urljoin(self.arxiv_base_url, dt.find_all(title="Abstract")[0]["href"])
            pdf_link = urljoin(self.arxiv_base_url, dt.find_all(title="Download PDF")[0]["href"])

            # extract the title (.title class in the dd tag)
            title = dd.find("div", class_="list-title").get_text(strip=True).replace("Title:", "")

            # extract author information (.authors class in dd tag)
            authors = dd.find("div", class_="list-authors").get_text(strip=True)

            # extract the abstract (.abstract class in dd tag)
            abstract = dd.find("p", class_="mathjax").get_text(strip=True)

            papers.append({
                "pdf_url": pdf_link,
                "html_url": html_link,
                "authors": authors,
                "title": title,
                "abstract": abstract
            })

        return papers

    def crawl_arxiv_papers_by_full_topic_list(self):
        full_papers = []
        for topic in self.arxiv_topic_list:
            papers = self.crawl_arxiv_papers_by_single_topic(topic)
            full_papers.extend(papers)

        return full_papers

    def save_arxiv_papers(self, full_papers, filename):
        current_date = datetime.now().strftime("%Y%m%d")
        filename = self.arxiv_papers_crawled_jsonl.format(current_date)

        with open(filename, "w", encoding="utf-8") as jsonl_file:
            for paper in full_papers:
                json.dump(paper, jsonl_file, ensure_ascii=False)
                jsonl_file.write("\n")

        return len(full_papers)

    def process_arxiv_papers_crawl(self):
        full_papers = self.crawl_arxiv_papers_by_full_topic_list()
        full_papers_count = self.save_arxiv_papers(full_papers, self.arxiv_papers_crawled_jsonl)

        return full_papers_count
    
if __name__ == '__main__':
    conf = init_environment_conf()
    
    arxiv_base_url = conf['arxiv']['arxiv_base_url']
    arxiv_topic_url = conf['arxiv']['arxiv_topic_url']
    arxiv_topic_list = conf['arxiv']['arxiv_topic_list']
    arxiv_papers_crawled_jsonl = conf['analysis']['arxiv_papers_crawled_jsonl']
    
    arxiv_papers_crawler = ArxivPapersCrawler(arxiv_base_url, arxiv_topic_url, arxiv_topic_list, arxiv_papers_crawled_jsonl)
    arxiv_papers_crawled_count = arxiv_papers_crawler.process_arxiv_papers_crawl()

    print(f"Arxiv Papers Crawl: Done! arxiv_papers_crawled_count: {arxiv_papers_crawled_count}")