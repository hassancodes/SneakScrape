def func():
    print("\n \n \n \n")


# requirements
import requests
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook







#
# headers = {"query" : stylecodeList[1:2][0]}
res = requests.get("https://www.goat.com/sneakers/ubiq-x-crazy-byw-2-0-sister-cities-ubiq-byw-2")

# print(res.cookies())
func()
print(res.content)
func()
