import json
from bs4 import BeautifulSoup
import requests
import json
import pprint
#

# testing
# 530455w05g01000
# 163363c
# 563731c
# 162987c
print("input style code: ")
stylecode = input()
request = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept-Language': 'en-US,en;q=0.5',
    }


# primary url-used to generate url from the response
primaryreq = request.get(f"https://www.goat.com/search?query={stylecode}",headers=headers)

print(primaryreq.status_code)
psoup = BeautifulSoup(primaryreq.content, "lxml")
print(psoup.prettify())



#
# res = request.get("https://www.goat.com/sneakers/gundam-x-dunk-high-sb-project-unicorn-rx-0-dh7717-100", headers=headers)
# soup = BeautifulSoup(res.content,"lxml")
#
# with open("index.html", "r") as file:
#     sp = BeautifulSoup(file.read(), 'lxml')
#     if len(sp.find_all("script"))==22:
#         scrp = sp.find("script")
#         dataJson = json.loads(scrp.contents[0])
#         brand = dataJson["brand"]
#         color = dataJson["color"]
#         name = dataJson["name"]
#         releaseDate = dataJson["releaseDate"]
#         print(name,color,brand,releaseDate)
#
#     else:
#         "Not Found"
