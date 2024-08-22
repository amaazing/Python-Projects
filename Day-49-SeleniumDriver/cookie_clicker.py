'''
Author: Maaz Ali
Date: August 22 2024
A bot to autoplay cookie clicker
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def buy(dict):
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
    print(f"You have {money} cookies")
    for item in dict:
        if money>dict[item]:
            item_logo = driver.find_element(By.ID, value=f"{item}")
            item_logo.click()
            print(f"You {item}!")
            break
    return

    

if __name__ == "__main__":    
    cookie = driver.find_element(By.ID, value="cookie") #Gets the cookie by id
    #Gets the shop items
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    items = [item.get_attribute("id") for item in store]
        
    #Gets the prices and converts to int
    prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_cost = []
    
    for price in prices:
        integer_price = (price.text.split("-")[-1].strip().replace(",", "")) #split is there because the prices originally contain both item name and cost.
        if integer_price != "":
            item_cost.append(int(integer_price))
            
    cookie_shop = {}
    for n in range(len(item_cost)-1, -1, -1):
        cookie_shop[items[n]] = item_cost[n]
    print(cookie_shop)
    
    time_left = time.time() + 5
    while True:
        if time.time()>time_left:
            buy(cookie_shop)
            time_left = time.time() + 5
        cookie.click()