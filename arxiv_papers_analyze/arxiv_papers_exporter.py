import json
from datetime import datetime
from arxiv_papers_utils import init_environment_conf

class ArxivPaperExporter:
    """
    Arxiv Paper Exporter
    Step3: export arxiv paper analyzed jsonl to markdown file
    """
    def __init__(self, arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md):
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl
        self.arxiv_papers_analyzed_md = arxiv_papers_analyzed_md

    def load_arxiv_paper_jsonl(self):
        papers = []
        with open(self.arxiv_papers_analyzed_md, "r", encoding="utf-8") as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                papers.append(data)
        return papers

    def export_arxiv_paper_md(self):
        current_date = datetime.now().strftime("%Y%m%d")
        arxiv_papers_analyzed_md = self.arxiv_papers_analyzed_md.format(current_date)
        arxiv_papers_analyzed_jsonl = self.arxiv_papers_analyzed_jsonl.format(current_date)

        full_papers_count = 0
        with open(arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file, open(arxiv_papers_analyzed_md, "w", encoding="utf-8") as md_file:
            for line in jsonl_file:
                data = json.loads(line)
                md_file.write(f"# {data['title']}\n")
                md_file.write(f"## Authors\n")
                md_file.write(f"{data['authors']}\n")
                md_file.write(f"## Abstract\n")
                md_file.write(f"{data['abstract']}\n")
                md_file.write(f"## Innovation\n")
                md_file.write(f"{data['innovation']}\n")
                md_file.write(f"## Conclusion\n")
                md_file.write(f"{data['conclusion']}\n")
                md_file.write(f"## PDF URL\n")
                md_file.write(f"{data['pdf_url']}\n")
                md_file.write(f"## HTML URL\n")
                md_file.write(f"{data['html_url']}\n")
                md_file.write(f"## PDF URL\n")
                md_file.write(f"{data['pdf_url']}\n")
                md_file.write(f"## HTML URL\n")
                md_file.write(f"{data['html_url']}\n")

                full_papers_count += 1

        return full_papers_count
    
    def process_arxiv_papers_export(self):
        papers = self.load_arxiv_paper_jsonl()
        full_papers_count = self.export_arxiv_paper_md(papers)

        return full_papers_count
    
if __name__ == '__main__':
    conf = init_environment_conf()

    arxiv_papers_analyzed_md = conf['analysis']['arxiv_papers_analyzed_md']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']

    arxiv_papers_exporter = ArxivPaperExporter(arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md)
    arxiv_papers_exported_count = arxiv_papers_exporter.process_arxiv_papers_export()

    print(f"Arxiv Papers Export Done! export {arxiv_papers_exported_count} arxiv papers")