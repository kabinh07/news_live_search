from scrapers.BaseScraper import BaseScraper
from scrapers.ManualSearchScraper import ManualSearchScraper

# url = "thehimalayantimes.com"
# keyword = "world+cup"
keyword = "খালেদা+জিয়া"
# url = f"https://www.deccanherald.com/search?q={keyword}"
# url = f"https://www.dailyjanakantha.com/"
# url = "https://www.kalbela.com/search/google/?q="
# url = "https://www.amadershomoy.com/search/?s="


url = "https://www.jaijaidinbd.com/"
search_keys ={
    "search_content": {
        "method": "id",
        "value": "search_result_block"
        },
    "search_nav": {
        "icon": {
            "method": "css_selector",
            "value": '.fa-magnifying-glass'
        },
        "bar": {
            "method": 'css_selector',
            "value": '.form-control'
        }
    }
}

# url = "https://www.kalbela.com/"
# search_keys ={
#     "search_content": {
#         "method": "id",
#         "value": "search_result_block"
#         },
#     "search_nav": {
#         "icon": {
#             "method": "css_selector",
#             "value": '#dropdownSearch > i:nth-child(1)'
#         },
#         "bar": {
#             "method": 'css_selector',
#             "value": '.form-control'
#         }
#     }
# }


# url = f"https://www.dailyjanakantha.com/"
# search_keys ={
#     "search_content": {
#         "method": "class",
#         "value": "gsc-resultsbox-visible"
#         },
#     "search_nav": {
#         "icon": {
#             "method": "css_selector",
#             "value": 'li.menu-search > a:nth-child(1) > i:nth-child(1)'
#         },
#         "bar": {
#             "method": 'css_selector',
#             "value": '.pl-0 > form:nth-child(1) > div:nth-child(1) > input:nth-child(4)'
#         }
#     }
# }
b = ManualSearchScraper()
b.setup(url, keyword, **search_keys)
news_urls = b.manual_search()
b.close_driver()
print(news_urls)