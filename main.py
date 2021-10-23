def func():
    print("\n \n \n \n")


# requirements
import requests
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook




styleCodes = load_workbook(filename="StyleCodes.xlsx")

print(dir(styleCodes))
func()
sheet = styleCodes.active
print(sheet)
func()

stylecodeList = [x.value for x in sheet["A"]]
print(stylecodeList[1:])



#
# headers = {"query" : stylecodeList[1:2][0]}
res = requests.get("https://www.goat.com/sneakers/ubiq-x-crazy-byw-2-0-sister-cities-ubiq-byw-2")

# print(res.cookies())
func()
print(res.content)
func()
