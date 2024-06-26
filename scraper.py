from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm

with open("categories.txt", "r") as f:
    categories = f.read().split("\n")

def get_domain(url):
    elms = url.split("/")
    for elm in elms:
        if ".com" in elm or ".net" in elm or ".in" in elm:
            return elm
    return

def news_validation(url):
    url_elms = url.split(".com")
    prefixes = url_elms[-1].split("/")
    try:
        if prefixes[1] in categories:
            if prefixes[1] != prefixes[-1] and prefixes[-1] not in categories:
                return True
    except:
        return False
    return False

with open("spam_sites.txt", "r") as f:
    spam_sites = f.read().split("\n")

def spam_check(url):
    if url in spam_sites:
        return False
    return True

def news_search(driver, input):
    content_class = "container"
    base_url = input["base_url"]
    content_class = input["content_cls"]
    domain = get_domain(base_url)
    print(f"Domain: {domain}")
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, content_class)))
    time.sleep(5)
    content = driver.find_element(By.CLASS_NAME, content_class)
    hlinks = content.find_elements(By.TAG_NAME, "a")
    for link in hlinks:
        url = link.get_attribute("href")
        # print(f"Raw URL: {url}")
        if domain in str(url):
            if spam_check(url):
                print(url)

def main():
    keyword = "বিশ্বকাপ"
    # keyword = "world+cup"
    # keyword = input("Enter your keyword: ")

    # # URLs
    # input = {
    #     "base_url": f"https://www.ucanews.com/home/googlesearch?q={keyword}&cx=partner-pub-001599941463365685814%3Asfheipyjbn0&cof=FORID%3A10&ie=ISO-8859-1&sa=Search",
    #     "content_cls" : "gsc-results-wrapper-overlay"
    # }
    # input = {
    #     "base_url": f"https://www.thestatesman.com/?s={keyword}",
    #     "content_cls" : "loop-grid-3"
    # }
    # input = {
    #     "base_url": f"https://www.thenews.com.pk/search1?cx=014389848304649563256%3Aureyfztd74a&cof=FORID%3A10&ie=UTF-8&q={keyword}",
    #     "content_cls" : "gsc-resultsbox-visible"
    # }
    # input = {
    #     "base_url": f"https://www.telegraphindia.com/search?search-term={keyword}",
    #     "content_cls" : "storylisting"
    # }
    # input = {
    #     "base_url": f"https://www.taiwannews.com.tw/search?keyword={keyword}",
    #     "content_cls" : "mainContainer"
    # }
    # input = {
    #     "base_url": f"https://www.sentinelassam.com/search?q={keyword}",
    #     "content_cls" : "list-component-m_list__MRP6o"
    # }
    # input = {
    #     "base_url": f"https://www.opindia.com/?s={keyword}",
    #     "content_cls" : "wpb_wrapper"
    # }
    # input = {
    #     "base_url": f"https://www.irrawaddy.com/?s={keyword}",
    #     "content_cls" : "jnews_search_content_wrapper"
    # }
    # input = {
    #     "base_url": f"https://www.deccanherald.com/search?q={keyword}",
    #     "content_cls" : "container"
    # }
    # input = {
    #     "base_url": f"https://www.dawn.com/search?cx=016184311056644083324%253Aa1i8yd7zymy&cof=FORID%253A10&ie=UTF-8&q={keyword}",
    #     "content_cls" : "gsc-results"
    # }
    # input = {
    #     "base_url": f"https://www.dailypioneer.com/searchlist.php?search={keyword}",
    #     "content_cls" : "highLightedNews"
    # }
    # input = {
    #     "base_url": f"https://www.altnews.in/?s={keyword}",
    #     "content_cls" : "content-area"
    # }
    # input = {
    #     "base_url": f"https://www.aa.com.tr/en/search/?s={keyword}",
    #     "content_cls" : "tab-content"
    # }
    # input = {
    #     "base_url": f"https://thepeninsulaqatar.com/news/search?q={keyword}",
    #     "content_cls" : "rel-news"
    # }
    # input = {
    #     "base_url": f"https://thehimalayantimes.com/search?query={keyword}",
    #     "content_cls" : "post_list"
    # }
    # input = {
    #     "base_url": f"https://scroll.in/search?q={keyword}",
    #     "content_cls" : "all-stories-container"
    # }
    # input = {
    #     "base_url": f"https://nenow.in/?s={keyword}",
    #     "content_cls" : "site-main"
    # }
    # input = {
    #     "base_url": f"https://www.amadershomoy.com/search/?s={keyword}",
    #     "content_cls" : "author-page-news"
    # }
    # input = {
    #     "base_url": f"https://bangla.thedailystar.net/search?t={keyword}",
    #     "content_cls" : "gsc-expansionArea"
    # }
    # input = {
    #     "base_url": f"https://bangla.dhakatribune.com/search?q={keyword}",
    #     "content_cls" : "gsc-webResult"
    # }
    # input = {
    #     "base_url": f"https://www.prothomalo.com/search?q={keyword}",
    #     "content_cls" : "_7rTOU"
    # }
    # input = {
    #     "base_url": f"https://www.ittefaq.com.bd/search?q={keyword}",
    #     "content_cls" : "gsc-webResult"
    # }
    # input = {
    #     "base_url": f"https://www.bd-pratidin.com/home/search?cx=5d07de91748e84546&cof=FORID%253A10&ie=UTF-8&q={keyword}",
    #     "content_cls" : "gsc-expansionArea"
    # }
    # input = {
    #     "base_url": f"https://samakal.com/search?q={keyword}",
    #     "content_cls" : "gsc-expansionArea"
    # }
    # input = {
    #     "base_url": f"https://www.ajkerpatrika.com/search?q={keyword}",
    #     "content_cls" : "gsc-webResult"
    # }
    # input = {
    #     "base_url": f"https://dailyinqilab.com/search?q={keyword}",
    #     "content_cls" : "gsc-expansionArea"
    # }
    input = {
        "base_url": f"https://cse.google.com/cse?cx=d540ac00b35dc4da6&ie=utf-8&q={keyword}",
        "content_cls" : "gsc-expansionArea"
    }
    


    driver = webdriver.Chrome()
    news_search(driver, input)
    driver.quit()

if __name__ == "__main__":
    main()

