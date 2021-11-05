import requests
from bs4 import BeautifulSoup
proxy = {
"http" : "us-dynamic-1.resdleafproxies.com:17133",
 "https" : "us-dynamic-1.resdleafproxies.com:17133"
}


headers = {
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
'Accept-Language': 'en-US,en;q=0.5',
}

cookies = {
'stockx_homepage': "sneakers",
}
res = requests.get("https://stockx.com/adidas-yeezy-foam-rnnr-ochre", headers=headers , cookies=cookies, proxies=proxy)
bod = BeautifulSoup(res.content, "lxml")
print(bod)
