import json
from datetime import datetime

class ArxivPaperExporter:
    """
    Arxiv Paper Exporter
    """
    def __init__(self, arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md):
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl
        self.arxiv_papers_analyzed_md = arxiv_papers_analyzed_md

    def export_arxiv_paper_md(self):
        current_date = datetime.now().strftime("%Y%m%d")
        arxiv_papers_analyzed_md = self.arxiv_papers_analyzed_md.format(current_date)
        arxiv_papers_analyzed_jsonl = self.arxiv_papers_analyzed_jsonl.format(current_date)

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
    