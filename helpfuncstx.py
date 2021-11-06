import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from fake_useragent import UserAgent
from random import randint
import random

####################################################################
####################################################################
# function to generate the main url.
# this functions converts - ""adidas Crazy BYW X 2.0 Ubiq" to "adidas-crazy-byw-x-2-ubiq"
# later we will connect this with stockx.com
def createUrl(SneakerName):
    ls = SneakerName.lower().split(" ")
    parsedls =[]
    for i in ls:
            if i.replace('.','').isdigit():
                parsedls.append(str(int(i.split(".")[0])))

            else:
                parsedls.append(i)
    endpoint = "-".join(parsedls)
    #
    return endpoint

######################################################################
######################################################################

# function for getting style codes from the excel sheet
def getStyleCode():
    styleCodes = load_workbook("StyleCodes.xlsx")
    sheet = styleCodes.active
    rawsdList = [x.value for x in sheet["A"]]
# main style code list
    StyleCodeList = rawsdList[1:]
    # print("Total Style codes: ",len(StyleCodeList))
    return StyleCodeList

#######################################################################
#######################################################################

# function for generating fake useragent
def ua():

    ua = UserAgent()
    return ua.chrome

def spacefunc():
    print("\n")


# getting the divs
def parseDiv(ls):
    for i in range(len(ls)):
        stripped = str(ls[i]).strip()[8:].strip()
        if stripped.startswith("window.__APOLLO_STATE_"):
            return ls[i]
            break
        else:
            pass

#######################################################################
#######################################################################

def parseIp():
    proxyList = []
    with open("ip.txt") as ip:
        for i in ip:
            iplist = i.split(":")
            readyProxy = "".join((iplist[0],":",iplist[1]))
            proxyList.append(readyProxy)


    random.shuffle(proxyList)
    return proxyList




# import requests
# url = 'https://api.myip.com'
# wIpList = parseIp()
# counter =
# proxy = {
# "http":wIpList[counter],
#  "https":wIpList[counter]
# }
#
# response = requests.get(url, proxies = proxy)
# print(response.json())



def randomIp(counter):
    ipList = parseIp()
    wIpList = ipList.copy()

    if counter<len(wIpList):
        # print(counter , ":<", wIpList[counter])
        return wIpList[counter]

    elif counter > 2*(len(wIpList)) :
        r = random.randint(0,len(wIpList)-1)
        # print(r , wIpList[r])
        # print("random: ", wIpList[r])
        return wIpList[r]

    elif counter==len(wIpList) or counter < 2*(len(wIpList)):
        # print(counter , ":=>", wIpList[len(wIpList)-counter] )
        return wIpList[len(wIpList)-counter]



# counter=0
# for i in range(0,1000):
#     counter +=1
#     print(i,"===",randomIp(i))
#     print("\n \n \n")
#
# print("LOL: ",counter)
