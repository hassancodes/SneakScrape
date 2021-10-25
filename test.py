import requests
from bs4 import BeautifulSoup
import pprint

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from helpfuncs
from helpfuncstx import createUrl


op = Options()

op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)
op.add_argument("start-maximized")




driver = webdriver.Chrome('./chromedriver', keep_alive=True, options=op)
driver.get("https://google.com")







# request start from here
# request = requests.Session()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
#     'Accept-Language': 'en-US,en;q=0.5'
#     }
#
# cookies = {
#     'stockx_homepage': "sneakers",
#     }
#
# soup = BeautifulSoup(request.get("https://stockx.com/search?s=eg6608", headers=headers, cookies=cookies).content,"lxml")
#
# bod = soup.body
# div = bod.find_all("div", class_="css-h8htgv")
#
# # checking for the first shoe
# a = div[0].find_all('p')
#
#
# # 2nd functions
# sneakNameprice = []
# for i in a:
#     sneakNameprice.append(i.get_text())
#
#
#
#
# # print(createUrl("adidas Crazy BYW X 2.0 Ubiq"))
# mainURL = f"https://stockx.com/{createUrl(sneakNameprice[0])}"
# print("timedelay...")
# time.sleep(10)
#
# # soupmain = BeautifulSoup(request.get(mainURL,headers=headers, cookies=cookies).content,"lxml")
# # pprint.pprint(soupmain.body)
# #
# # print(soupmain.body)
# #
# # print("\n \n \n \n \n")
# # bodmain = soupmain.body
# # divmain = bodmain.find_all("div", class_="css-1s359ds")
# #
# # print(len(divmain))
# #
# # print(divmain)
#
# driver.get("")














#
# <div class="css-h8htgv">
#    <style data-emotion="css 1c5ij41">.css-1c5ij41{margin:16px;}</style>
#    <div class="css-1c5ij41">
#       <style data-emotion="css 1d8x81o">.css-1d8x81o{width:140px;height:75px;max-width:100%;margin:0px auto;}</style>
#       <div class="css-1d8x81o"></div>
#    </div>
#    <style data-emotion="css 1r242c2">.css-1r242c2{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:var(--chakra-colors-neutral-100);padding:var(--chakra-space-4);text-align:left;}</style>
#    <style data-emotion="css mi73i9">.css-mi73i9{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:var(--chakra-colors-neutral-100);padding:var(--chakra-space-4);text-align:left;}</style>
#    <div class="css-mi73i9">
#       <style data-emotion="css 1x3b5qq">.css-1x3b5qq{color:var(--chakra-colors-neutral-black);font-size:var(--chakra-fontSizes-xs);font-weight:var(--chakra-fontWeights-medium);line-height:1.3;height:2.75rem;overflow:hidden;}@media screen and (min-width: 30em){.css-1x3b5qq{font-size:var(--chakra-fontSizes-sm);height:3.5rem;}}@media screen and (min-width: 48em){.css-1x3b5qq{height:3.5rem;}}</style>
#       <p class="css-1x3b5qq">adidas Crazy BYW X 2.0 Ubiq</p>
#       <div>
#          <div class="price-line-div">
#             <style data-emotion="css 1d3ta0m">.css-1d3ta0m{color:var(--chakra-colors-neutral-500);text-transform:capitalize;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);overflow:hidden;margin-top:0.25rem;line-height:1.3;}</style>
#             <style data-emotion="css 1joryfz">.css-1joryfz{font-family:var(--chakra-fonts-suisseIntlRegular);line-height:var(--chakra-lineHeights-md);letter-spacing:0.004rem;color:var(--chakra-colors-neutral-500);text-transform:capitalize;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);overflow:hidden;margin-top:0.25rem;line-height:1.3;}</style>
#             <p class="chakra-text css-1joryfz">lowest ask</p>
#             <style data-emotion="css eiug9l">.css-eiug9l{color:var(--chakra-colors-neutral-black);font-size:var(--chakra-fontSizes-md);font-family:var(--chakra-fonts-suisseIntlMedium);line-height:1.3;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}@media screen and (min-width: 30em){.css-eiug9l{font-size:var(--chakra-fontSizes-xl);}}</style>
#             <style data-emotion="css 1kph905">.css-1kph905{font-family:var(--chakra-fonts-suisseIntlRegular);line-height:var(--chakra-lineHeights-md);letter-spacing:0.004rem;color:var(--chakra-colors-neutral-black);font-size:var(--chakra-fontSizes-md);font-family:var(--chakra-fonts-suisseIntlMedium);line-height:1.3;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}@media screen and (min-width: 30em){.css-1kph905{font-size:var(--chakra-fontSizes-xl);}}</style>
#             <p class="chakra-text css-1kph905">$75</p>
#          </div>
#       </div>
#       <style data-emotion="css 1n60jv3">.css-1n60jv3{color:var(--chakra-colors-neutral-500);text-transform:capitalize;line-height:1.3;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);white-space:nowrap;margin-right:var(--chakra-space-1);line-height:1.3;}</style>
#       <style data-emotion="css 5a0v95">.css-5a0v95{font-family:var(--chakra-fonts-suisseIntlRegular);line-height:var(--chakra-lineHeights-md);letter-spacing:0.004rem;color:var(--chakra-colors-neutral-500);text-transform:capitalize;line-height:1.3;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);white-space:nowrap;margin-right:var(--chakra-space-1);line-height:1.3;}</style>
#       <p class="chakra-text css-5a0v95"></p>
#       <style data-emotion="css 4c36c">.css-4c36c{color:var(--chakra-colors-neutral-500);text-transform:capitalize;line-height:1.3;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);white-space:nowrap;line-height:1.3;overflow:hidden;text-overflow:ellipsis;}</style>
#       <style data-emotion="css 1eaqka8">.css-1eaqka8{font-family:var(--chakra-fonts-suisseIntlRegular);line-height:var(--chakra-lineHeights-md);letter-spacing:0.004rem;color:var(--chakra-colors-neutral-500);text-transform:capitalize;line-height:1.3;font-size:var(--chakra-fontSizes-xs);font-family:var(--chakra-fonts-suisseIntlMedium);white-space:nowrap;line-height:1.3;overflow:hidden;text-overflow:ellipsis;}</style>
#       <p class="chakra-text css-1eaqka8"> </p>
#    </div>
# </div>
# '''
