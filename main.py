#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

####### Example 1

# resp = requests.get("https://encrypted.google.com/async/flights_origin_destination?async=origin:CCU,destination:BLR,departure_date:2017-10-14,return_date:2017-10-20,is_oneway:false")

# content = resp.content
# soup = BeautifulSoup(content, "html.parser")

# for s in soup:
#  print(s[2])

# print("style" in soup)


####### Example 2 #######

# Variable initialize
BASE_URL = "https://rubygarage.org"
PAGE_NUMBER = "1"
PAGE_QUERY = "?page=" + PAGE_NUMBER
BLOG_URL = BASE_URL + "/blog" + PAGE_QUERY
data = {}
tag = {}

rBlog = requests.get(BLOG_URL)
rBlogContent = rBlog.content

# Soup insrance containing blog cotent
soup = BeautifulSoup(rBlogContent, "html.parser")

# All card items
cardItmes = soup.findAll("div", { "class": "card-item"})

# Loop througth card items
for cardItme in cardItmes:
    # grabi tag logo
    data["logo"] = cardItme.find("img")["src"]
    # extract title using class
    cardBlogTitle = cardItme.find("div", { "class": "card-blog__title"})
    # grab link from tag title
    data["link"] = BASE_URL + cardBlogTitle.find("a")["href"]
    # grab title from link text
    data["title"] = cardBlogTitle.find("a").text
    # extract tag using class
    cardBlogTag = cardItme.find("div", { "class": "card-blog__tags"})
    # extrct li of tag 
    cardBlogTagList = cardBlogTag.find("ul").findAll("li")
    # grab tag name
    tag["name"] = cardBlogTagList[0].find("a").text
    # grab tag link
    tag["link"] = cardBlogTagList[0].find("a")["href"]
    # grab tag views
    tag["views"] = cardBlogTagList[1].text
    # assign tag object into main data object
    data["tag"] = tag
    # display data
    print(data)