from selenium import webdriver
import time 
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/@nevguba")

time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.prettify())