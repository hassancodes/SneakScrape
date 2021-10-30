import requests
from bs4 import BeautifulSoup
import pprint
import json

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from helpfuncs
from helpfuncstx import createUrl
from useragent import ua

def func():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

# op = Options()
# op.add_experimental_option("excludeSwitches", ["enable-automation"])
# op.add_experimental_option('useAutomationExtension', False)
# op.add_argument("start-maximized")
# op.add_argument(r"user-data-dir=C:\Users\hassa\AppData\Local\Google\Chrome Dev\User Data\ninja")
#
#
#
# driver = webdriver.Chrome('./chromedriver', keep_alive=True, options=op)
# driver.get("https://google.com")
#
# driver.implicitly_wait(10)
#
# driver.get("https://github.com")


# request main function

request = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept-Language': 'en-US,en;q=0.5',
    }

cookies = {
    'stockx_homepage': "sneakers",
    }

time.sleep(10)


# logic needs to be added keep chaning the shoe style

soup = BeautifulSoup(request.get("https://stockx.com/search?s=GW3355", headers=headers, cookies=cookies).content,"lxml")

bod = soup.body
div = bod.find_all("div", class_="css-h8htgv")

# checking for the first shoe
a = div[0].find_all('p')

print(a)

# 2nd functions
# this list will have title, prize and one thing more that I forgot
sneakNameprice = []
for i in a:
    sneakNameprice.append(i.get_text())



print(sneakNameprice)
func()
# print(createUrl("adidas Crazy BYW X 2.0 Ubiq"))


mainURL = f"https://stockx.com/{createUrl(sneakNameprice[0])}"
# print(mainURL)
func()
print("timedelay...")
time.sleep(10)

soupmain = BeautifulSoup(request.get(mainURL,headers=headers, cookies=cookies).content,"lxml")

time.sleep(10)
# pprint.pprint(soupmain.body)

# print(soupmain.body)

bodmain = soupmain.body
# print(bodmain)
func()


# print(soupmain.body)
scriptmain = bodmain.find_all("script")
print("Length of script main: " , len(scriptmain))
# getting the script with index
scriptindex = scriptmain[7]
print("ScriptIndex : ", scriptindex)


# print(str(scriptindex)[37:-13].strip())
# using bs4 again to re itterate over the script tag
# jsoup = BeautifulSoup(scriptindex, "lxml")

# removing the tags and trailing spaces
rawjson = str(scriptindex)[41:-15].strip()
pprint.pprint(rawjson)
func()
print("raw json")
print(type(rawjson))


#
#
#
rjsoup = BeautifulSoup(rawjson, "lxml")

print("rjsoup:" , rjsoup)
print(type(rjsoup))


readyDict = {}

with open("data.json" , "w") as dj:
    readyJson = json.loads(rjsoup.text)
    func()
    # ready json is main json that have the data but still need to be cleaned
    print("readyJson: " , readyJson)
    func()
    json.dump(readyJson,dj)
    print("successfully added to file")

    func()

    for i in readyJson:
        if i.startswith("Product"):
            print(i)

            func()

            readyDict["title"] = readyJson[i]["primaryTitle"]
            readyDict["brand"] = readyJson[i]["brand"]
            readyDict["traits"]  = readyJson[i]["traits"]

            # contains the url for the shoes, it maybe helpful so i added it into the sheet
            readyDict["media"]  = readyJson[i]["media"]["imageUrl"]

        else:
            pass

print(readyDict)






# required exact keys to target from ready json
# "primaryTitle"
# "Traits" (required data for excel is in here)
# "styleId"
# "brand"
# "Media" to get the url and image

lol = {'title': 'Nike Dunk Low', 'brand': 'Nike', 'traits': [{'__typename': 'Traits', 'name': 'Style', 'value': 'DD1391-003'}, {'__typename': 'Traits', 'name': 'Colorway', 'value': 'Midnight Navy/Championship Grey-White'}, {'__typename': 'Traits', 'name': 'Retail Price', 'value': '100'}, {'__typename': 'Traits', 'name': 'Release Date', 'value': '2021-11-05'}, {'__typename': 'Traits', 'name': 'Featured', 'value': 'false'}], 'media': {'__typename': 'Media', 'imageUrl': 'https://images.stockx.com/images/Nike-Dunk-Low-Georgetown-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1634918141', 'smallImageUrl': 'https://images.stockx.com/images/Nike-Dunk-Low-Georgetown-Product.jpg?fit=fill&bg=FFFFFF&w=300&h=214&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1634918141', 'gallery': [], 'all360Images': ['https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img01.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img02.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img03.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img04.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img05.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img06.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img07.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img08.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img09.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img10.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img11.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img12.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img13.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img14.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img15.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img16.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img17.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img18.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img19.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img20.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img21.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img22.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img23.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img24.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img25.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img26.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img27.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img28.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img29.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img30.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img31.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img32.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img33.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img34.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img35.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141', 'https://images.stockx.com/360/Nike-Dunk-Low-Georgetown/Images/Nike-Dunk-Low-Georgetown/Lv2/img36.jpg?auto=format,compress&w=559&q=90&dpr=2&updated_at=1634918141'], 'thumbUrl': 'https://images.stockx.com/images/Nike-Dunk-Low-Georgetown-Product.jpg?fit=fill&bg=FFFFFF&w=140&h=100&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1634918141'}}







# # fetching scripts
# # 35435:36173
