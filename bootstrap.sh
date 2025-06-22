#!/bin/bash

# current date
current_date=$(date +%Y%m%d)
export CURRENT_DATE=$current_date

# step1: crawl arxiv papers
python3 arxiv_papers_analyze/arxiv_papers_crawler.py --conf bootstrap.yaml

# step2: analyze arxiv papers
python3 arxiv_papers_analyze/arxiv_papers_analyst.py --conf bootstrap.yaml

# step3: export arxiv papers to markdown
python3 arxiv_papers_analyze/arxiv_papers_exporter.py --conf bootstrap.yaml

