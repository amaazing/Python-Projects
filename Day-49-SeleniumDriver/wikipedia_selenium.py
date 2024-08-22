'''
Author: Maaz Ali
Practice using selenium webdriver
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_statistics = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

#article_statistics.click()

portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#portals.click()

search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_icon.click()
search_bar = driver.find_element(By.NAME, value = "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)