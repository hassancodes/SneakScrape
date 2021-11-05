import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl import Workbook
import pprint,json,time,random
# help functions are all present in helpfuncstx.py
from helpfuncstx import createUrl, getStyleCode, ua,spacefunc



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
###############################################################################################################
###############################################################################################################
# you can add proxies here
    # proxies = {
    #
    # }
    soup = BeautifulSoup(request.get(f"https://stockx.com/search?s={stylecode}", headers=headers, cookies=cookies).content,"lxml")
    bod = soup.body
    div = bod.find_all("div", class_="css-h8htgv")
    # checking for the first shoe
    try:
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
            print(scriptindex)
            rawjson = str(scriptindex)[41:-15].strip()
            return rawjson


        elif len(scriptlist) == 27:
            scriptindex = scriptlist[6]
            rawjson = str(scriptindex)[41:-15].strip()
            return rawjson
        elif len(scriptlist) == 24:
            print(scriptlist)
        else:
            rawjson = {}
            return rawjson
    except:
        return {}



def parseJson(rawjson):

    if rawjson == {}:
        return {}
    elif rawjson != {}:
        rjsoup = BeautifulSoup(rawjson, "lxml")
        print(rjsoup)
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

# # need to work here tomorrow
# ["Not Found" for x in mydict if mydict.get("traits")[x].get("name") !="Style" else mydict["traits"][0]["value"]]
        title = "Not Found" if mydict.get("title")==None else mydict["title"]
        brand = "Not Found" if mydict.get("brand")==None else mydict["brand"]
        url = "Not Found" if mydict.get("media")==None else mydict["media"]


        sequence = ["Style" ,"Colorway" , "Retail Price","Release Date" ]
        dataList = []
        # function for seperating the found data from the "not found elements"
        def checkFound(ls):
            if all(element == ls[0] for element in ls):
                dataList.append("Not Found")
            else:
                list(filter(lambda x: dataList.append(x) if x!="Not Found" else "pass",ls))




        for i in sequence:
            # this list contains the items, if not present in the json  fetched by the web it will be replaced by "not Found"
            rawList = [mydict["traits"][x]["value"] if mydict.get("traits")[x].get("name")==i else "Not Found" for x in range(len(mydict.get("traits")))]
            checkFound(rawList)
        print(dataList)
        styleId = dataList[0]
        colorway = dataList[1]
        price = dataList[2]
        releaseDate = dataList[3]



        # adding data to excel indices
        sheet[f"B{counter}"] = title
        sheet[f"C{counter}"] = colorway
        sheet[f"D{counter}"] = price
        sheet[f"E{counter}"] = releaseDate
        sheet[f"F{counter}"] = brand
        sheet[f"G{counter}"] = url

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

# #main logic
stylecodelist = getStyleCode()
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
