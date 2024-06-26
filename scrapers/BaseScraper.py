from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

opts = ChromeOptions()
opts.add_argument("--window-size=1900,1080")
opts.page_load_strategy = "eager"

class BaseScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=opts)
        self.news_links = []
    
    def setup(self, url, keyword, **kwargs):
        self.base_url = url
        self.keyword = keyword
        self.attr = kwargs

        # print(self.attr)

    def get_domain(self):
        elms = self.base_url.split("/")
        for elm in elms:
            if ".com" in elm or ".net" in elm or ".in" in elm:
                return elm
        return
    
    def close_driver(self):
        self.driver.quit()

    def news_search(self):
        domain = self.get_domain()
        print(f"Domain: {domain}")
        self.driver.get(self.base_url+self.keyword)
        time.sleep(5)
        try:
            if self.attr["method"] == "class":
                print("Inside class method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.attr["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.CLASS_NAME, self.attr["value"])
            elif self.attr["method"] == "id":
                print("Inside id method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.attr["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.ID, self.attr["value"])
            elif self.attr["method"] == "xpath":
                print("Inside xpath method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.attr["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.XPATH, self.attr["value"])
            elif self.attr["method"] == "css_selector":
                print("Inside css method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.attr["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.CSS_SELECTOR, self.attr["value"])
            else:
                print("Inside NULL method")
                return
        except Exception as e:
            print(e)
            return
        hlinks = content.find_elements(By.TAG_NAME, "a")
        for link in hlinks:
            url = link.get_attribute("href")
            if domain in str(url):
                self.news_links.append(url)
        news = set(self.news_links)

        self.close_driver()
        return list(news)

    def close_driver(self):
        self.driver.quit()