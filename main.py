#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://encrypted.google.com/async/flights_origin_destination?async=origin:CCU,destination:BLR,departure_date:2017-10-14,return_date:2017-10-20,is_oneway:false")

content = resp.content
soup = BeautifulSoup(content, "html.parser")

# for s in soup:
#     print(s[2])

