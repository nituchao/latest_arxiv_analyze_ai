[![Python](https://img.shields.io/badge/Python-3.9%7C3.10%7C3.11%7C3.12%7C3.13-blue)](https://github.com/nituchao/latest_arxiv_analyze_ai/)
[![PyPI](https://badge.fury.io/py/tensorflow.svg)](https://badge.fury.io/py/tensorflow)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4724125.svg)](https://doi.org/10.5281/zenodo.4724125)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1486/badge)](https://bestpractices.coreinfrastructure.org/projects/1486)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/tensorflow/tensorflow/badge)](https://securityscorecards.dev/viewer/?uri=github.com/tensorflow/tensorflow)
[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/tensorflow.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:tensorflow)
[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/tensorflow-py.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:tensorflow-py)
[![OSSRank](https://shields.io/endpoint?url=https://ossrank.com/shield/44)](https://ossrank.com/p/44)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

**`Documentation`** |
------------------- |
[![Documentation](https://img.shields.io/badge/api-reference-blue.svg)](https://www.tensorflow.org/api_docs/) |

# Introduction
Analyze the latest papers on arXiv using large language models.

The lasted arxiv papers will be crawled and analyzed by topics, eg: cs.AI, cs.LG, stat.ML, etc.

You can fork this repo to run the code on your github actions workflow to analyze the latest arxiv papers automatically.

# arXiv Papers

The following fields will be exported to markdown file and rss/atom file:

| topic | title | title_en | authors | background | innovation | conclusion |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |

## RSS
You can subscribe to the latest papers using an RSS reader daily:

<a href="https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/rss.xml" target="_blank">RSS</a> | <a href="https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/atom.xml" target="_blank">ATOM</a>

## Markdown
You can subscribe to the latest papers using an Markdown reader daily:

[20250622](arxiv_papers_data/arxiv_papers_20250622_analyzed_Chinese.md) - 5 arxiv papers
