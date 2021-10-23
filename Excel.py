# file for working with excel
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

# function for getting style codes from the excel sheet
def getStyteCode():

    styleCodes = load_workbook(filename="StyleCodes.xlsx")
    sheet = styleCodes.active
    print(sheet)

    rawsdList = [x.value for x in sheet["A"]]
# main style code list
    StyleCodeList = rawsdList[1:]

    # print("Total Style codes: ",len(StyleCodeList))
    return StyleCodeList
