from iglovikov_helper_functions.config_parsing.utils import object_from_dict
from addict import Dict as Addict
import yaml
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import logging

logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("api_logs.log")

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

with open("config.yaml") as f:
    config = Addict(yaml.load(f, Loader=yaml.SafeLoader))

keys = config.inputs.keys()

keyword = "world+cup"

threads = []
news_urls = []

# def create_threads(config):
#     scraper = object_from_dict(config)
#     urls = scraper.news_search(keyword)
#     news_urls.extend(urls)
#     scraper.close_driver()

scrapers = []
for key in keys:
    scraper = object_from_dict(config.inputs[key])
    scrapers.append(scraper)

with ThreadPoolExecutor(max_workers=5) as exc:
    results = {exc.submit(scr.news_search, keyword): scr for scr in scrapers}
    for r in as_completed(results):
        print(r.result())

# for key in keys:
#     current_config = config.inputs[key]
#     thread = threading.Thread(target=create_threads, args=(current_config, ))
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()


