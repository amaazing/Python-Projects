'''
Author Maaz
Project using beautifulsoup
Finds the top Zelda games on metacritic.
'''
import requests
from bs4 import BeautifulSoup

headermap = {"User-Agent": "Windows Firefox"}
r = requests.get("https://www.metacritic.com/search/zelda/", headers=headermap)
content = r.text
beautiful_content = BeautifulSoup(content, "html.parser")
relevant_content = beautiful_content.find_all("div", "u-text-overflow-ellipsis")
relevant_score = beautiful_content.find_all("div", "c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_medium")

title_list = []
for titles in relevant_content:
    title_list.append(titles.find("p").text.strip())

score_list = []
for score in relevant_score:
    score_list.append(score.find("span").text)
    
score_length = len(score_list)
title_score = {title_list[i]:score_list[i] for i in range(0, score_length)}
print(title_score)