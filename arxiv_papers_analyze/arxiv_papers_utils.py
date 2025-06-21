import argparse
import yaml

def init_environment_conf():
    parser = argparse.ArgumentParser()

    parser.add_argument("--conf", type=str, required=True, help="the path of conf file, eg: bootstrap_conf.yaml")
    args = parser.parse_args()

    with open(args.conf, "r", encoding="utf-8") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)
    
    return conf