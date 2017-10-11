#!/usr/bin/env python3

from sys import argv
import requests
from bs4 import BeautifulSoup
from decorator import *

# Variable initialize
BASE_URL = "https://rubygarage.org"
PAGE_QUERY = ""
data = {}
tag = {}

@execute
def main():
    # read comman line
    for i in range(len(argv)):
        if argv[i] == "-p" or argv[i] == "-page":
            PAGE_QUERY = "page={}".format(argv[i+1])
            break
        else:
            PAGE_QUERY = "page=1"

    # make blog url       
    BLOG_URL = BASE_URL + "/blog?" + PAGE_QUERY

    # request blog
    rBlog = requests.get(BLOG_URL)
    # get blog content(html)
    rBlogContent = rBlog.content

    # Soup insrance containing blog cotent
    soup = BeautifulSoup(rBlogContent, "html.parser")

    # All card items
    cardItmes = soup.findAll("div", { "class": "card-item"})

    # Loop througth card items
    for cardItme in cardItmes:
        # grab tag logo
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

if __name__ == "__main__":
    main()