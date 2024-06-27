from iglovikov_helper_functions.config_parsing.utils import object_from_dict
from addict import Dict as Addict
import yaml

with open("config.yaml") as f:
    config = Addict(yaml.load(f, Loader=yaml.SafeLoader))

print(config)

b = object_from_dict(config.inputs.thestatesman)
urls = b.news_search("world+cup")
print(urls)
