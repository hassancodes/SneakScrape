import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl import Workbook
import pprint,json,time,random
# help functions are all present in helpfuncstx.py
from helpfuncstx import createUrl, getStyteCode, ua,spacefunc


def fetchsource(stylecode):
    # starting my session
    request = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Accept-Language': 'en-US,en;q=0.5',
        }

    cookies = {
        'stockx_homepage': "sneakers",
        }
    soup = BeautifulSoup(request.get(f"https://stockx.com/search?s={stylecode}", headers=headers, cookies=cookies).content,"lxml")
    bod = soup.body
    div = bod.find_all("div", class_="css-h8htgv")
    # checking for the first shoe
    a = div[0].find_all('p')
    # print(a)

    # 2nd functions
    # this list will have title, prize and one thing more that I forgot
    sneakdatalist = []
    for i in a:
        sneakdatalist.append(i.get_text())
    print(sneakdatalist)
    spacefunc()
    # generating product page link by using createUrl function
    mainURL = f"https://stockx.com/{createUrl(sneakdatalist[0])}"
    # print(mainURL)
    print("timedelay...")
    time.sleep(10)
    soupmain = BeautifulSoup(request.get(mainURL,headers=headers, cookies=cookies).content,"lxml")
    # pprint.pprint(soupmain.body)
    # print(soupmain.body)
    scriptlist = soupmain.body.find_all("script")
    print("Length of script Lists: " , len(scriptlist))
    spacefunc()
    # getting the script with index

    if len(scriptlist) ==28:
        scriptindex = scriptlist[7]
        rawjson = str(scriptindex)[41:-15].strip()
        return rawjson

    elif len(scriptlist) == 27:
        scriptindex = scriptlist[6]
        rawjson = str(scriptindex)[41:-15].strip()
        return rawjson
    else:
        rawjson = {}
        return rawjson



def parseJson(rawjson):

    if rawjson == {}:
        return {}
    elif rawjson != {}:

        rjsoup = BeautifulSoup(rawjson, "lxml")

        # print("rjsoup:" , rjsoup)
        # print(type(rjsoup))
        readyDict = {}

        with open("data.json" , "w") as dj:

            readyJson = json.loads(rjsoup.text)
            # ready json is main json that have the data but still need to be cleaned
            # print("readyJson: " , readyJson)
            spacefunc()
            json.dump(readyJson,dj)
            print("successfully added the json to data.json")
            for i in readyJson:
                if i.startswith("Product"):
                    print(i)
                    # title aka name
                    readyDict["title"] = readyJson[i]["primaryTitle"]
                    readyDict["brand"] = readyJson[i]["brand"]
                    readyDict["traits"]  = readyJson[i]["traits"]

                    # contains the url for the shoes, it maybe helpful so i added it into the sheet
                    readyDict["media"]  = readyJson[i]["media"]["imageUrl"]
                else:
                    pass

    return readyDict

####################################################################
def addtoExcel(mydict,counter):
    print(f"scraping {counter} entry....")
    # adding 1 so we can match with the excel index
    counter +=1
    stylecodes = load_workbook(filename="StyleCodes.xlsx")
    sheet = stylecodes.worksheets[0]
    # uselessly validation 😂 but necessary
    if  len(mydict)>2:

# need to work here tomorrow
        title = "Not Found" if mydict.get("title")==None else mydict["title"]
        brand = "Not Found" if mydict.get("brand")==None else mydict["brand"]
        url = "Not Found" if mydict.get("media")==None else mydict["media"]
        styleId = "Not Found" if mydict.get("traits")[0].get("name") !="Style" else mydict["traits"][0]["value"]
        colorway = "Not Found" if mydict.get("traits")[1].get("name") !="Colorway" else mydict["traits"][1]["value"]
        price = "Not Found" if mydict.get("traits")[2].get("name") !="Retail Price" else mydict["traits"][2]["value"]
        releaseDate = "Not Found" if mydict.get("traits")[3].get("name") !="Release Date" else mydict["traits"][3]["value"]

        # adding data to excel indices
        sheet[f"B{counter}"] = title
        sheet[f"C{counter}"] = colorway
        sheet[f"D{counter}"] = price
        sheet[f"E{counter}"] = releaseDate
        sheet[f"F{counter}"] = brand

        print(f"added data to index {counter}")
    else:

        sheet[f"B{counter}"] = "Not found"
        sheet[f"C{counter}"] = "Not found"
        sheet[f"D{counter}"] = "Not found"
        sheet[f"E{counter}"] = "Not found"
        sheet[f"F{counter}"] = "Not found"
        print(f"index {counter} Not found")

    stylecodes.save("StyleCodes.xlsx")

# # [Style Code	Name	Color	Price	Release Date	Brand]

# # main logic
stylecodelist = getStyteCode()
# stylecodelist = ["eg6608","b41990", "b22537"]
def iterate(sclist):
    for i in range(len(sclist)):
        counter = i+1
        rawjson = fetchsource(sclist[i])
        readydict = parseJson(rawjson)
        # make sure to add a counter
        addtoExcel(readydict,counter)
        time.sleep(random.randint(50,100))


iterate(stylecodelist)




# ######## required exact keys to target from ready json  #############
# "primaryTitle"                                                      #
# "Traits" (required data for excel is in here)                       #
# "styleId"                                                           #
# "brand"                                                             #
# "Media" to get the url and image                                    #
# #####################################################################
# # fetching scripts
# # 35435:36173
