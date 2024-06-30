from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import logging

logger = logging.getLogger("api_logger")

opts = ChromeOptions()
opts.add_argument("--window-size=1900,1080")
opts.add_argument("--headless")
opts.page_load_strategy = "normal"

class BaseScraper:
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(options=opts)
        self.news_links = []
        self.attr = kwargs
        self.base_url = self.attr["url"]

    def get_domain(self):
        elms = self.base_url.split("/")
        for elm in elms:
            if ".com" in elm or ".net" in elm or ".in" in elm:
                return elm
        return
    
    def close_driver(self):
        self.driver.quit()

    def news_search(self, keyword):
        domain = self.get_domain()
        logger.info(f"Domain: {domain}")
        logger.info(self.base_url+keyword)
        self.driver.get(self.base_url+keyword)
        time.sleep(5)
        try:
            if self.attr["search_content"]["method"] == "class":
                logger.info("Inside class method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.attr["search_content"]["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.CLASS_NAME, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "id":
                logger.info("Inside id method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.attr["search_content"]["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.ID, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "xpath":
                logger.info("Inside xpath method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.attr["search_content"]["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.XPATH, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "css_selector":
                logger.info("Inside css method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.attr["search_content"]["value"])))
                time.sleep(1)
                content = self.driver.find_element(By.CSS_SELECTOR, self.attr["search_content"]["value"])
            else:
                logger.info("Inside NULL method")
                return
        except Exception as e:
            logger.info(e)
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