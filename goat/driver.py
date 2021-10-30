import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Own files
from Excel import getStyteCode



styleCodes = getStyteCode()

# function to get cookies using requests
# def getcookies():
#     rs = requests.Session()
#     res = rs.get("https://www.goat.com/")
#     # print(res.headers)
#     return dict(res.cookies)

def parseCookies(selcookies):
    cookies = {}
    for k,v in selcookies.items():
        cookies[str(k)] = str(v)
    return cookies








driver = webdriver.Chrome('./chromedriver', keep_alive=True)
# add different style codes later
driver.get("https://www.goat.com/search?query=eg6608")
driver.implicitly_wait(10)



# driverCookies  = driver.get_cookies()
# print(driverCookies)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div/div[3]/div[4]/div/ul/div[1]/div[1]/div/a/div/div/div[3]").click()
driver.implicitly_wait(5)

driver.refresh();

driver.implicitly_wait(5)

driver.refresh();
# rs = requests.Session()
# cookies = parseCookies(driverCookies[0])
# print()
# print("cookies from functions : " ,cookies)
# print()
# res = rs.get("https://www.goat.com/sneakers/ubiq-x-crazy-byw-2-0-sister-cities-ubiq-byw-2" ,cookies=cookies)
# print(res.status_code)
#
# print("\n")
# print(res.content)
# print("\n")
#
# print(res.text)




    # a = driver.page_source
    # print(a)
# elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div/div[3]/div[4]/div/ul/div[1]/div[1]/div/a/div/div/div[3]/h2")
# print(elem.get_attribute('innerHTML'))
#
#
# ubiq-x-crazy-byw-2-0-sister-cities-ubiq-byw-2
# UBIQ x Crazy BYW 2.0 'Sister Cities'

# print(driver.page_source)

# with open("index.html", "r") as fp:
#     soup = BeautifulSoup(fp, features ="html.parser")
#     # print(soup)
#     # bod = soup.body.find("div",{"class": "ProductTemplateGridCell__GridCell-sc-1yrb6b3-4 jOxZrp"})
#     bod = soup.find_all('div')
#     print(bod)
