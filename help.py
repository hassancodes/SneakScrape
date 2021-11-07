# import json
# with open("data.json",'r') as fp:
#     readyJson = json.load(fp)
#     readyDict = {}
#     # for i in readyJson:
#     #     if not (readyJson[i].get('traits') is None):
#     #         readyDict["title"] = readyJson[i]["primaryTitle"]
#     #         readyDict["brand"] = readyJson[i]["brand"]
#     #         readyDict["traits"]  = readyJson[i]["traits"]
#     #         readyDict["media"]  = readyJson[i]["media"]["imageUrl"]
#     #     else:
#     #         print("\n \n \n")
#     #         print(i)
#     #         pass
#
#     targetList = []
#     for i in readyJson:
#         if i.startswith("Product"):
#             targetList.append(i)
#
#     print(targetList)
#     print("\n \n \n")
#     for prod in targetList:
#         if not (readyJson[prod].get('traits') is None):
#             readyDict["title"] = readyJson[prod]["primaryTitle"]
#             readyDict["brand"] = readyJson[prod]["brand"]
#             readyDict["traits"]  = readyJson[prod]["traits"]
#             readyDict["media"]  = readyJson[prod]["media"]["imageUrl"]
#             break
#         else:
#             pass
#
#     print(readyDict)

import requests
try:
    a = requests.get("https://google.com" ,timeout=10)
except requests.exceptions.ConnectTimeout:
    print({})

print(a.status_code)
