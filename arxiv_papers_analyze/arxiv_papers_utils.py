from email.utils import format_datetime
from datetime import datetime
from pytz import timezone
import argparse
import yaml

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

if __name__ == "__main__":
    
    print(get_date_rfc822_string())
