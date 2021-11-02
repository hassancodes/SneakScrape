mydict = {
"primaryTitle": "adidas Crazy BYW X 2.0",
"secondaryTitle": "Ubiq",
"condition": "New",
"brand": "adidas",
"has360Images": False,
"model": "adidas Crazy BYW X 2.0",
"description": "",
"styleId": "EG6608",
"traits": [{
"__typename": "Traits",
"name": "Style",
"value": "EG6608"
}, {
"__typename": "Traits",
"name": "Colorway",
"value": "Footwear White/Solar Yellow/Core Black"
}, {
"__typename": "Traits",
"name": "Retail Price",
"value": "170"
}, {
"__typename": "Traits",
"name": "Release Date",
"value": "2019-12-14"
}, {
"__typename": "Traits",
"name": "Featured",
"value": "false"
}]
}



sequence = ["Style" ,"Colorway" , "Retail Price","Release Date" ]

# function for seperating the found data from the "not found elements"
def checkFound(ls):
    if all(element == ls[0] for element in ls):
        dataList.append("Not Found")
    else:
        list(filter(lambda x: dataList.append(x) if x!="Not Found" else "pass",ls))


dataList = []
for i in sequence:
    als = [mydict["traits"][x]["value"] if mydict.get("traits")[x].get("name")==i else "Not Found" for x in range(len(mydict.get("traits")))]
    checkFound(als)






print(dataList)
