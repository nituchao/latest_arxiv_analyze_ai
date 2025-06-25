<div  align="center">    
<img src="static/imgs/arxiv-logo.png" alt="arXiv" align=center />
<br/>
</div>

[![last-commit](https://img.shields.io/github/last-commit/nituchao/latest_arxiv_analyze_ai?logo=github&color=32CD32)](https://github.com/nituchao/latest_arxiv_analyze_ai/)
[![arxiv_papers_analyze](https://github.com/nituchao/latest_arxiv_analyze_ai/actions/workflows/arxiv_papers_analyze.yml/badge.svg?color=32CD32)](https://github.com/nituchao/latest_arxiv_analyze_ai/actions/workflows/arxiv_papers_analyze.yml)
[![OpenAI|LLM|Agent](https://img.shields.io/badge/OpenAI-LLM|Agent-FF00FF)](https://github.com/nituchao/latest_arxiv_analyze_ai/)
[![Python](https://img.shields.io/badge/Python-3.9~3.13-1E90FF)](https://github.com/nituchao/latest_arxiv_analyze_ai/)
[![ATOM|RSS](https://img.shields.io/badge/ATOM%7CRSS-Subscribe-00CED1)](https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/rss.xml)
[![Markdown](https://img.shields.io/badge/Markdown-Static-00BFFF)](https://github.com/nituchao/latest_arxiv_analyze_ai/)


# Introduction
Analyze and give a summary of latest papers on arXiv using LLM(large language models) by daily.

The latest arXiv papers will be crawled and analyzed by topic (e.g., `cs.AI`, `cs.LG`, `stat.ML`, etc.), and LLM will be used to extract `background`, `innovation`, and `conclusion`. The results will be exported daily as markdown files and rss/atom files.

You can also fork this repo to run the code on your local machine or Github actions workflow to analyze the latest arXiv papers automatically.

# arXiv Papers

The following fields will be exported to markdown file and rss/atom file:

<table>
    <thead>
        <tr>
            <th>topic</th>
            <th>title</th>
            <th>authors</th>
            <th>background</th>
            <th>innovation</th>
            <th>conclusion</th>
        </tr>
    </thead>
</table>

## ATOM/RSS
You can subscribe to the fllowing atom/rss source to get the latest papers analyzed by AI on daily:

 [![Static Badge](https://img.shields.io/badge/ATOM-Press_To_Subscribe%20%7C%20Recommended-00CED1)](https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/atom.xml) 👈 

[![Static Badge](https://img.shields.io/badge/RSS-Press_To_Subscribe-00CED1)](https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/rss.xml) 

[Zotero](https://www.zotero.org/) is a cross-platform(Mac, Windows, Linux, iOS, and Android) reference management tool that can be used to manage your references. You can also use it to import the arxiv papers from atom/rss.

[Readkit](https://readkit.app/) is a cross-platform app(Mac, iOS, iPad) that can sync subscriptions, articles and read statuses between platforms if you use one of the supported feed aggregators or read-later services.

<div align="center">
  <img src="static/imgs/zotero-rss-20250625.jpeg" alt="zotero" height="200">
  <img src="static/imgs/readkit-rss-20250625.jpeg" alt="readkit" height="200">
</div>

## Markdown
The latest arxiv papers will be analyzed by AI on daily and listed as below:


[20250625](arxiv_papers_data/arxiv_papers_20250625_analyzed_Chinese.md) - 219 arxiv papers 

[20250624](arxiv_papers_data/arxiv_papers_20250624_analyzed_Chinese.md) - 444 arxiv papers 

[20250623](arxiv_papers_data/arxiv_papers_20250623_analyzed_Chinese.md) - 371 arxiv papers 

[20250622](arxiv_papers_data/arxiv_papers_20250622_analyzed_Chinese.md) - 219 arxiv papers
