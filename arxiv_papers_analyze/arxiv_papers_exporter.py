import os
import json
from arxiv_papers_utils import init_environment_conf, get_date_string

class ArxivPaperExporter:
    """
    Arxiv Paper Exporter
    Step3: export arxiv paper analyzed jsonl to markdown file
    """
    def __init__(self, arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md, arxiv_analysis_language, current_date):
        self.current_date = current_date
        self.arxiv_analysis_language = arxiv_analysis_language
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl.format(current_date)
        self.arxiv_papers_analyzed_md = arxiv_papers_analyzed_md.format(current_date, arxiv_analysis_language)

    def export_arxiv_paper_md(self):

        full_papers_count = 0
        with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file, open(self.arxiv_papers_analyzed_md, "w", encoding="utf-8") as md_file:
            for idx, line in enumerate(jsonl_file, start=1):
                data = json.loads(line)
                md_file.write(f"# {idx}. `{data['topic']}` - {data['title']} [PDF]({data['pdf_url']}), [HTML]({data['html_url']})\n")
                md_file.write(f"## Authors\n")
                md_file.write(f"{data['authors']}\n")
                md_file.write(f"## Background\n")
                md_file.write(f"{data['background']}\n")
                md_file.write(f"## Innovation\n")
                md_file.write(f"{data['innovation']}\n")
                md_file.write(f"## Conclusion\n")
                md_file.write(f"{data['conclusion']}\n")

                full_papers_count += 1

        return full_papers_count
    
    def export_arxiv_paper_readme(self, arxiv_papers_exported_count):
        
        new_paper_line = f"\n[{self.current_date}_{self.arxiv_analysis_language}]({self.arxiv_papers_analyzed_md}) - {arxiv_papers_exported_count} arxiv papers\n"

        try:
            with open('README.md', 'r', encoding="utf-8") as f:
                lines = f.readlines()

            new_paper_line_idx = lines.index("# arXiv Papers\n") + 5
            lines.insert(new_paper_line_idx, new_paper_line)

            with open('README.md', 'w', encoding="utf-8") as f:
                f.writelines(lines)
        except FileNotFoundError:
            lines = []
    
    def process_arxiv_papers_export(self):
        full_papers_count = self.export_arxiv_paper_md()

        return full_papers_count
    
if __name__ == '__main__':
    conf = init_environment_conf()

    arxiv_analysis_language = conf['analysis']['arxiv_analysis_language']
    arxiv_papers_analyzed_md = conf['analysis']['arxiv_papers_analyzed_md']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']

    current_date = os.environ.get('current_date', get_date_string()).strip()

    arxiv_papers_exporter = ArxivPaperExporter(arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md, arxiv_analysis_language, current_date)
    arxiv_papers_exported_count = arxiv_papers_exporter.process_arxiv_papers_export()
    arxiv_papers_exporter.export_arxiv_paper_readme(arxiv_papers_exported_count)

    print(f"Arxiv Papers Export Done! export {arxiv_papers_exported_count} arxiv papers")