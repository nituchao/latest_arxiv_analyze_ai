import yaml
import argparse
from arxiv_papers_analyze.arxiv_papers_crawler import ArxivPapersCrawler
from arxiv_papers_analyze.arxiv_papers_analyst import ArxivPaperAnalyst
from arxiv_papers_analyze.arxiv_papers_exporter import ArxivPaperExporter

def init_environment_conf():
    parser = argparse.ArgumentParser()

    parser.add_argument("--conf", type=str, required=True, help="the path of conf file, eg: bootstrap_conf.yaml")
    args = parser.parse_args()

    with open(args.conf, "r", encoding="utf-8") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)
    
    return conf

def analyze_arxiv_papers(conf):
    arxiv_base_url = conf['arxiv']['arxiv_base_url']
    arxiv_topic_url = conf['arxiv']['arxiv_topic_url']
    arxiv_topic_list = conf['arxiv']['arxiv_topic_list']
    arxiv_papers_crawled_jsonl = conf['analysis']['arxiv_papers_crawled_jsonl']
    arxiv_papers_crawler = ArxivPapersCrawler(arxiv_base_url, arxiv_topic_url, arxiv_topic_list, arxiv_papers_crawled_jsonl)
    #arxiv_papers_crawled_count = arxiv_papers_crawler.process_arxiv_papers_crawl()

    llm_api_key = conf['llm']['api_key']
    llm_base_url = conf['llm']['base_url']
    llm_model_name = conf['llm']['model_name']
    prompt_user = conf['prompt']['user']
    prompt_system = conf['prompt']['system']
    arxiv_analysis_language = conf['analysis']['arxiv_analysis_language']
    arxiv_papers_analyzed_jsonl = conf['analysis']['arxiv_papers_analyzed_jsonl']
    arxiv_papers_analyst = ArxivPaperAnalyst(arxiv_papers_crawled_jsonl, llm_api_key, llm_base_url, llm_model_name, arxiv_analysis_language, prompt_system, prompt_user, arxiv_papers_analyzed_jsonl)
    arxiv_papers_analyzed_count = arxiv_papers_analyst.process_arxiv_papers_analyze()

    arxiv_papers_analyzed_md = conf['analysis']['arxiv_papers_analyzed_md']
    arxiv_papers_exporter = ArxivPaperExporter(arxiv_papers_analyzed_jsonl, arxiv_papers_analyzed_md)
    arxiv_papers_exported_count = arxiv_papers_exporter.process_arxiv_papers_export()

    print(f"arxiv_papers_crawled_count: {arxiv_papers_crawled_count}, arxiv_papers_analyzed_count: {arxiv_papers_analyzed_count}, arxiv_papers_exported_count: {arxiv_papers_exported_count}")

if __name__ == '__main__':
    conf = init_environment_conf()
    analyze_arxiv_papers(conf)
