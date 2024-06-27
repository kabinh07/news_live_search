from iglovikov_helper_functions.config_parsing.utils import object_from_dict
from addict import Dict as Addict
import yaml
import threading

with open("config.yaml") as f:
    config = Addict(yaml.load(f, Loader=yaml.SafeLoader))

keys = config.inputs.keys()

keyword = "world+cup"

threads = []
news_urls = []

def create_threads(config):
    scraper = object_from_dict(config)
    urls = scraper.news_search(keyword)
    news_urls.extend(urls)
    scraper.close_driver()

for key in keys:
    current_config = config.inputs[key]
    thread = threading.Thread(target=create_threads, args=(current_config, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(len(news_urls))
print(news_urls)


