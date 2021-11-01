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

print(type(mydict))

# "mango" if i%3==0 else "orange" for i in range(10)


ls = [mydict["traits"][x]["value"] if mydict.get("traits")[x].get("name")=="Release Date" else "Not Found" for x in range(len(mydict.get("traits")))]
print(ls)
