from email.utils import format_datetime
from datetime import datetime
from pytz import timezone
import argparse
import yaml
import re

def init_environment_conf():
    parser = argparse.ArgumentParser()

    parser.add_argument("--conf", type=str, required=True, help="the path of conf file, eg: bootstrap_conf.yaml")
    args = parser.parse_args()

    with open(args.conf, "r", encoding="utf-8") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)
    
    return conf

def get_date_string(dt=None, fmt='%Y%m%d', tz=timezone('Asia/Shanghai')):
    if dt is None:
        return datetime.now(tz).strftime(fmt)
    return dt.strftime(fmt)

def get_date_rfc822_string(dt=None, tz=timezone('Asia/Shanghai')):
    
    if dt is None:
        dt = datetime.now(tz)
    date_rfc822 = format_datetime(dt)

    return date_rfc822

def get_date_rfc3339_string(dt=None, tz=timezone('Asia/Shanghai')):
    if dt is None:
        dt = datetime.now(tz)
    
    return dt.isoformat(timespec='seconds')

def get_arxiv_papers_feed_atom_entry(id, title, link, topic, summary, content, modified):
    entry_atom = f"""<entry><id>{id}</id><title>{title}</title><link href="{link}" rel="alternate" type="text/html" /><summary>{summary}</summary><content>{content}</content><updated>{modified}</updated><category term="{topic}" /></entry>"""

    return entry_atom

def get_arxiv_papers_feed_atom_message(entry_content):
    title = f"Arxiv Papers Analyze AI"
    modified = f"{get_date_rfc3339_string()}"
    id = f"https://github.com/nituchao/latest_arxiv_analyze_ai"

    feed_atom = f"""<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>{title}</title><link rel="self" type="application/atom+xml" href="https://nituchao.github.io/latest_arxiv_analyze_ai/arxiv_papers_data/atom.xml"/><link rel="alternate" type="text/html" hreflang="en" href="https://github.com/nituchao/latest_arxiv_analyze_ai"/><updated>{modified}</updated><id>{id}</id>{entry_content}</feed>"""

    return feed_atom

def convert_c_escapes_to_ascii(c_string: str) -> str:
    C_ESCAPE_MAP = {
        'a': 'a',  # BEL (0x07)
        'b': 'b',  # BS (0x08)
        'f': 'f',  # FF (0x0C)
        'n': 'n',  # LF (0x0A)
        'r': 'r',  # CR (0x0D)
        't': 't',  # HT (0x09)
        'v': 'v',  # VT (0x0B)
        '\\': '?',  # \
        '"': '?',   # "
        "'": "?",   # '
    }
    escape_pattern = re.compile(r'\\([abfnrtv\\"\' ])')
    
    def replace_match(match: re.Match) -> str:
        escape_char = match.group(1)
        return C_ESCAPE_MAP.get(escape_char, match.group(0))
    
    return escape_pattern.sub(replace_match, c_string)