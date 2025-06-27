import re
import os
import json
import PyRSS2Gen
from datetime import datetime
from xml.sax.saxutils import escape
from arxiv_papers_utils import init_environment_conf, get_date_string, get_date_rfc822_string, get_date_rfc3339_string, get_arxiv_papers_feed_atom_entry, get_arxiv_papers_feed_atom_message, convert_c_escapes_to_ascii

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

        try:
            full_papers_count = 0
            
            with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file:
                json_lines = jsonl_file.readlines()
            
            with open(self.arxiv_papers_analyzed_md, "w", encoding="utf-8") as md_file:
                for idx, line in enumerate(json_lines, start=1):
                    try:
                        if not self.check_required_files(line):
                            raise ValueError(f"required fields not found in line: {line}")

                        line = line.replace("\\n", "").replace("\n", "")
                        line = convert_c_escapes_to_ascii(line)
                        data = json.loads(line)
                        md_file.write(f"# {self.current_date}\n[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)\n\n")
                        md_file.write(f"## {idx}. `{data['topic']}` - {data['title']} [PDF]({data['pdf_url']}), [HTML]({data['html_url']})\n")
                        md_file.write(f"### Authors\n")
                        md_file.write(f"{data['authors']}\n")
                        md_file.write(f"### Background\n")
                        md_file.write(f"{data['background']}\n")
                        md_file.write(f"### Innovation\n")
                        md_file.write(f"{data['innovation']}\n")
                        md_file.write(f"### Conclusion\n")
                        md_file.write(f"{data['conclusion']}\n")
                    except Exception as e:
                        print(f"idx: {idx}, error happens: {e}, skip this paper, line: {line}")

                    full_papers_count += 1

            print(f"Arxiv Papers Export to [markdown] Done! {full_papers_count} arxiv papers have been exported to markdown file.")

            return full_papers_count
        except Exception as e:
            print(f"export_arxiv_paper_to_markdown error: {e}")
            return 0
    
    def export_arxiv_paper_to_rss(self):

        try:
            items = []
            with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file:
                jsonl_lines = jsonl_file.readlines()
                jsonl_lines.reverse()
                
                for idx, line in enumerate(jsonl_lines, start=1):
                    try:
                        if not self.check_required_files(line):
                            raise ValueError(f"required fields not found in line: {line}")
                        
                        line = convert_c_escapes_to_ascii(line)
                        data = json.loads(line)
        
                        id = escape(f"{data['pdf_url']}")
                        topic = escape(f"{data['topic']}")
                        title = escape(f"{idx}. {topic}-{data['title']}")
                        link = escape(f"{data['pdf_url']}")
                        lastBuildDate = get_date_rfc822_string(data['llm_update_time'])
                        content = escape(f"Background: \n{data['background']}\n\nInnovation: \n{data['innovation']}\n\nConclusion: \n{data['conclusion']}<a href='https://github.com/nituchao/latest_arxiv_analyze_ai' ><img src='https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss' alt='Visitors' title='Visitors'></a>")

                        item = PyRSS2Gen.RSSItem(  
                            title = title,  
                            link = link,  
                            description = content,
                            guid = PyRSS2Gen.Guid(id),  
                            pubDate = lastBuildDate
                        )
                        items.append(item)
                    except Exception as e:
                        print(f"idx: {idx}, error happens: {e}, skip this paper, line: {line}")
                        
            rss = PyRSS2Gen.RSS2(
                title = "Arxiv Papers Analyze AI",
                link = "https://github.com/nituchao/latest_arxiv_analyze_ai",
                description = f"Arxiv papers analyzed by AI on {self.current_date}",
                lastBuildDate = lastBuildDate,
                items = items,
            )

            rss.write_xml(open(f"{self.arxiv_papers_rss}", "w", encoding="utf-8"), encoding='utf-8')

            print(f"Arxiv Papers Export to [rss.xml] Done! {len(items)} arxiv papers have been exported to markdown file.")
        except Exception as e:
            print(f"export_arxiv_paper_to_rss2gen error: {e}")

    def export_arxiv_paper_to_atom(self):

        try:
            atom_entry_list = []
            with open(self.arxiv_papers_analyzed_jsonl, "r", encoding="utf-8") as jsonl_file:
                jsonl_lines = jsonl_file.readlines()
                jsonl_lines.reverse()
                
                for idx, line in enumerate(jsonl_lines, start=1):
                    try:
                        line = convert_c_escapes_to_ascii(line)
                        data = json.loads(line)

                        id = escape(f"{data['pdf_url']}")
                        topic = escape(f"{data['topic']}")
                        link = escape(f"{data['pdf_url']}")
                        author = escape(f"{data['authors']}")
                        title = escape(f"{idx}. {topic}-{data['title']}")
                        llm_update_time = escape(f"{data['llm_update_time']}")
                        
                        summary = escape(f"{data['background']}")
                        content = escape(f"Background: <br>{data['background']}<br><br>Innovation: <br>{data['innovation']}<br><br>Conclusion: <br>{data['conclusion']}<a href='https://github.com/nituchao/latest_arxiv_analyze_ai' ><img src='https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss' alt='Visitors' title='Visitors'></a>")
                        entry = get_arxiv_papers_feed_atom_entry(id, title, link, author, topic, summary, content, llm_update_time)
                        
                        atom_entry_list.append(entry)
                    except Exception as e:
                        print(f"idx: {idx}, error happens: {e}, skip this paper, line: {line}")

            atom_entry_str = "".join(atom_entry_list)
            atom_message = get_arxiv_papers_feed_atom_message(atom_entry_str)

            with open(self.arxiv_papers_atom, "w", encoding="utf-8") as atom_file:
                atom_file.write(atom_message)

            print(f"Arxiv Papers Export to [atom.xml] Done! {len(atom_entry_list)} arxiv papers have been exported to atom file.")
        except Exception as e:
            print(f"export_arxiv_paper_to_atom error: {e}")

    def find_first_line_startswith(self, file_lines, anchor_str):

        anchor_line = ""
        anchor_line_id = -1
        for line_id, line in enumerate(file_lines, start=0):
            if line.strip().startswith(anchor_str):
                anchor_line_id = line_id
                anchor_line = line
                break

        return anchor_line_id, anchor_line

    def export_arxiv_paper_to_readme(self, arxiv_papers_exported_count):
        anchor_str = f"![Static Badge](https://img.shields.io/badge/Markdown-arXivPaper-00BFFF)"
        new_paper_line = f"[![Static Badge](https://img.shields.io/badge/{self.current_date}-{arxiv_papers_exported_count}_Papers-32CD32)](https://github.com/nituchao/latest_arxiv_analyze_ai/blob/main/arxiv_papers_data/arxiv_papers_{self.current_date}_analyzed_Chinese.md)"

        try:
            with open('README.md', 'r', encoding="utf-8") as f:
                lines = f.readlines()

            anchor_line_id, anchor_line = self.find_first_line_startswith(lines, anchor_str)
            if anchor_line == "" or anchor_line_id == -1:
                print("Arxiv Papers Export to [readme] Fail! matched_line_id not found, skip.")
                return

            anchor_line_items = anchor_line.split("    ")
            anchor_line_items.insert(1, new_paper_line)
            
            anchor_line = "    ".join(anchor_line_items)
            lines[anchor_line_id] = anchor_line

            with open('README.md', 'w', encoding="utf-8") as f:
                f.writelines(lines)

            print(f"Arxiv Papers Export to [readme] Done! current_date: {self.current_date}.")
        except FileNotFoundError:
            lines = []
    
if __name__ == '__main__':
    conf = init_environment_conf()

    arxiv_papers_rss = conf['analysis']['arxiv_papers_rss']
    arxiv_papers_atom = conf['analysis']['arxiv_papers_atom']

    arxiv_analysis_language = conf['analysis']['arxiv_analysis_language']
    arxiv_papers_analyzed_md = conf['analysis']['arxiv_papers_analyzed_md']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']

    current_date = os.environ.get('CURRENT_DATE', get_date_string()).strip()

    arxiv_papers_exporter = ArxivPaperExporter(arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md, arxiv_papers_rss, arxiv_papers_atom, arxiv_analysis_language, current_date)

    # export arxiv papers to markdown, readme, rss, atom
    arxiv_papers_exported_count = arxiv_papers_exporter.export_arxiv_paper_to_markdown()
    arxiv_papers_exporter.export_arxiv_paper_to_readme(arxiv_papers_exported_count)
    arxiv_papers_exporter.export_arxiv_paper_to_atom()
    arxiv_papers_exporter.export_arxiv_paper_to_rss()

    print(f"Arxiv Papers Export Done! export {arxiv_papers_exported_count} arxiv papers, current date: {current_date}")
