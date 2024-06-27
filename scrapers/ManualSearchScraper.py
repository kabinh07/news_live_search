from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
from .BaseScraper import BaseScraper

class ManualSearchScraper(BaseScraper):
    def manual_search(self):
        self.driver.get(self.base_url)
        if self.attr["search_nav"]["icon"]["method"] == "class":
            search_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.attr["search_nav"]["icon"]["value"])))
            search_icon.click()
            time.sleep(1)
        elif self.attr["search_nav"]["icon"]["method"] == "id":
            search_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.attr["search_nav"]["icon"]["value"])))
            search_icon.click()
            time.sleep(1)
        elif self.attr["search_nav"]["icon"]["method"] == "xpath":
            search_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.attr["search_nav"]["icon"]["value"])))
            search_icon.click()
            time.sleep(1)
        elif self.attr["search_nav"]["icon"]["method"] == "css_selector":
            search_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.attr["search_nav"]["icon"]["value"])))
            search_icon.click()
            time.sleep(1)
        else:
            print("Inside NULL method")
            return
        
        if self.attr["search_nav"]["icon"]["method"] == "class":
            search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.attr["search_nav"]["bar"]["value"])))
            search_bar.send_keys(self.keyword)
            time.sleep(1)
            search_bar.send_keys(Keys.RETURN)
        elif self.attr["search_nav"]["icon"]["method"] == "id":
            search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.attr["search_nav"]["bar"]["value"])))
            search_bar.send_keys(self.keyword)
            time.sleep(1)
            search_bar.send_keys(Keys.RETURN)
        elif self.attr["search_nav"]["icon"]["method"] == "xpath":
            search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.attr["search_nav"]["bar"]["value"])))
            search_bar.send_keys(self.keyword)
            time.sleep(1)
            search_bar.send_keys(Keys.RETURN)
        elif self.attr["search_nav"]["icon"]["method"] == "css_selector":
            search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.attr["search_nav"]["bar"]["value"])))
            search_bar.send_keys(self.keyword)
            time.sleep(1)
            search_bar.send_keys(Keys.RETURN)
        else:
            print("Inside NULL method")
            return
        tabs = self.driver.window_handles
        print(len(tabs))
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[1])
            print(self.driver.title)
        domain = self.get_domain()
        print(f"Domain: {domain}")
        print(self.driver.current_url)
        time.sleep(5)
        print(self.driver.current_url)
        try:
            if self.attr["search_content"]["method"] == "class":
                print("Inside class method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.attr["search_content"]["value"])))
                content = self.driver.find_element(By.CLASS_NAME, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "id":
                print("Inside id method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.attr["search_content"]["value"])))
                content = self.driver.find_element(By.ID, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "xpath":
                print("Inside xpath method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.attr["search_content"]["value"])))
                content = self.driver.find_element(By.XPATH, self.attr["search_content"]["value"])
            elif self.attr["search_content"]["method"] == "css_selector":
                print("Inside css method")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.attr["search_content"]["value"])))
                content = self.driver.find_element(By.CSS_SELECTOR, self.attr["search_content"]["value"])
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
