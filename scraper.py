from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm

with open("categories.txt", "r") as f:
    categories = f.read().split("\n")

def get_domain(url):
    elms = url.split("/")
    for elm in elms:
        if ".com" in elm or ".net" in elm:
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

def news_search(driver, base_url):
    domain = get_domain(base_url)
    print(f"Domain: {domain}")
    driver.get(base_url)
    time.sleep(5)
    hlinks = driver.find_elements(By.TAG_NAME, "a")
    for link in tqdm(hlinks, total = len(hlinks)):
        url = link.get_attribute("href")
        # print(f"Raw URL: {url}")
        if domain in str(url):
            valid = news_validation(url)
            if valid:
                print(url)

def main():
    # keyword = "বিশ্বকাপ"
    keyword = input("Enter your keyword: ")
    base_url = f"https://www.prothomalo.com/search?q={keyword}"
    # base_url = f"https://samakal.com/search?q={keyword}"
    # base_url = f"https://www.ucanews.com/home/googlesearch?q={keyword}"
    # base_url = f"https://www.thestatesman.com/?s={keyword}"
    # base_url = f"https://www.thedailystar.net/search?t={keyword}"

    print(categories)

    driver = webdriver.Chrome()
    news_search(driver, base_url)
    driver.quit()

if __name__ == "__main__":
    main()

