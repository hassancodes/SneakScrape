import requests
from bs4 import BeautifulSoup
import pprint
import json
import time


# help functions are all present in helpfuncstx.py
from helpfuncstx import createUrl,getStyteCode
from useragent import ua

def func():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")


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

scriptmain = bodmain.find_all("script")
print("Length of script main: " , len(scriptmain))
# getting the script with index
scriptindex = scriptmain[7]
# print("ScriptIndex : ", scriptindex)

# removing the tags and trailing spaces
rawjson = str(scriptindex)[41:-15].strip()
pprint.pprint(rawjson)
func()
# print("raw json")
# print(type(rawjson))


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

            # title aka name
            readyDict["title"] = readyJson[i]["primaryTitle"]
            readyDict["brand"] = readyJson[i]["brand"]
            readyDict["traits"]  = readyJson[i]["traits"]

            # contains the url for the shoes, it maybe helpful so i added it into the sheet
            readyDict["media"]  = readyJson[i]["media"]["imageUrl"]
        else:
            pass

pprint.pprint(readyDict)

# function to parse dictionary
# def parseDict(dict):
    # for k,v in dict.items():










# ######## required exact keys to target from ready json  #############
# "primaryTitle"                                                      #
# "Traits" (required data for excel is in here)                       #
# "styleId"                                                           #
# "brand"                                                             #
# "Media" to get the url and image                                    #
# #####################################################################
# # fetching scripts
# # 35435:36173
