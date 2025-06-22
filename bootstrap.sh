#!/bin/bash

# current date
current_date=$(date +%Y%m%d)

# step1: crawl arxiv papers
python3 arxiv_papers_analyze/arxiv_papers_crawler.py --conf bootstrap.yaml --current_date $current_date

# step2: analyze arxiv papers
python3 arxiv_papers_analyze/arxiv_papers_analyst.py --conf bootstrap.yaml --current_date $current_date

# step3: export arxiv papers to markdown
python3 arxiv_papers_analyze/arxiv_papers_exporter.py --conf bootstrap.yaml --current_date $current_date