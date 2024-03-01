from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = 'https://news.google.com'
driver.get(url)
titles = driver.find_elements("//a[@class='DY5T1d']")
for title in titles:
    print(title.text)
    print(title.get_attribute('href'))

driver.quit()