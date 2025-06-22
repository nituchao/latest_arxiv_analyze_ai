import os
import json
from feedgen.feed import FeedGenerator
from arxiv_papers_utils import init_environment_conf, get_date_string, get_date_rfc822_string

class ArxivPaperExporter:
    """
    Arxiv Paper Exporter
    Step3: export arxiv paper analyzed jsonl to markdown file
    """
    def __init__(self, arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md, arxiv_papers_rss, arxiv_papers_atom, arxiv_analysis_language, current_date):
        self.current_date = current_date
        self.arxiv_papers_rss = arxiv_papers_rss
        self.arxiv_papers_atom = arxiv_papers_atom
        self.arxiv_analysis_language = arxiv_analysis_language
        self.arxiv_papers_analyzed_jsonl = arxiv_papers_analyzed_jsonl.format(current_date)
        self.arxiv_papers_analyzed_md = arxiv_papers_analyzed_md.format(current_date, arxiv_analysis_language)

    def check_required_files(self, line):
        data = json.loads(line)

        required_fields = ['topic', 'title', 'title_en', 'authors', 'background', 'innovation', 'conclusion', 'pdf_url', 'html_url']
        for field in required_fields:
            if field not in data:
                return False
            
            if data[field].strip() == "":
                return False
            
        return True

    def export_arxiv_paper_to_markdown(self):

        full_papers_count = 0
        with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file, open(self.arxiv_papers_analyzed_md, "w", encoding="utf-8") as md_file:
            for idx, line in enumerate(jsonl_file, start=1):
                try:
                    if not self.check_required_files(line):
                        raise ValueError(f"required fields not found in line: {line}")

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
                except Exception as e:
                    print(f"idx: {idx}, error happens: {e}, skip this paper, line: {line}")

                full_papers_count += 1

        return full_papers_count
    
    def export_arxiv_paper_to_rss(self, arxiv_papers_exported_count):
        fg = FeedGenerator()
        fg.language('zh-cn')
        fg.author({'name': 'nituchao'})
        fg.id('https://www.github.com/nituchao')
        fg.title(f"The latest arXiv papers analyzed by AI")
        fg.description(f"Arxiv papers analyzed by AI on {self.current_date}")
        fg.link(href='https://github.com/nituchao/latest_arXiv_analyze_ai', rel='alternate')
        fg.link(href='https://github.com/nituchao/latest_arXiv_analyze_ai/arxiv_papers_data/atom.xml', rel='self')

        with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file:
            jsonl_lines = jsonl_file.readlines()
            jsonl_lines.reverse()

            idx = 0
            for line in jsonl_lines:
                try:
                    if not self.check_required_files(line):
                        raise ValueError(f"required fields not found in line: {line}")
                    
                    data = json.loads(line)
    
                    fe = fg.add_entry()
                    fe.id(f"{arxiv_papers_exported_count - idx}. {data['title']}")
                    fe.title(f"{arxiv_papers_exported_count - idx}. {data['title']}")
                    fe.updated(get_date_rfc822_string())
                    fe.category(term=data['topic'])
                    fe.link(href=data['pdf_url'])
                    
                    fe.summary(f"{data['background']}")
                    fe.content(f"{data['innovation']}\n{data['conclusion']}", type='CDATA')
                    fe.pubDate(get_date_rfc822_string())
                except Exception as e:
                    print(f"idx: {idx}, error happens: {e}, skip this paper, line: {line}")
                    
                idx += 1

        # fg.atom_file(self.arxiv_papers_atom, encoding="utf-8") # Write the ATOM feed to a file
        fg.rss_file(self.arxiv_papers_rss, encoding="utf-8") # Write the RSS feed to a file

    def export_arxiv_paper_to_readme(self, arxiv_papers_exported_count):
        
        new_paper_line = f"\n[{self.current_date}]({self.arxiv_papers_analyzed_md}) - {arxiv_papers_exported_count} arxiv papers\n"

        try:
            with open('README.md', 'r', encoding="utf-8") as f:
                lines = f.readlines()

            new_paper_line_idx = lines.index("The lastest arxiv papers will be analyzed by AI on daily and listed as below:\n") + 2
            lines.insert(new_paper_line_idx, new_paper_line)

            with open('README.md', 'w', encoding="utf-8") as f:
                f.writelines(lines)
        except FileNotFoundError:
            lines = []
    
    def process_arxiv_papers_export(self):
        full_papers_count = self.export_arxiv_paper_to_markdown()

        return full_papers_count
    
if __name__ == '__main__':
    conf = init_environment_conf()

    arxiv_papers_rss = conf['analysis']['arxiv_papers_rss']
    arxiv_papers_atom = conf['analysis']['arxiv_papers_atom']

    arxiv_analysis_language = conf['analysis']['arxiv_analysis_language']
    arxiv_papers_analyzed_md = conf['analysis']['arxiv_papers_analyzed_md']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']

    current_date = os.environ.get('CURRENT_DATE', get_date_string()).strip()

    print(f"current_date: {current_date}")

    arxiv_papers_exporter = ArxivPaperExporter(arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md, arxiv_papers_rss, arxiv_papers_atom, arxiv_analysis_language, current_date)
    arxiv_papers_exported_count = arxiv_papers_exporter.process_arxiv_papers_export()
    arxiv_papers_exporter.export_arxiv_paper_to_readme(arxiv_papers_exported_count)
    # arxiv_papers_exporter.export_arxiv_paper_to_rss(arxiv_papers_exported_count)

    print(f"Arxiv Papers Export Done! export {arxiv_papers_exported_count} arxiv papers")
