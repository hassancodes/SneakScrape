import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from fake_useragent import UserAgent


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
def getStyteCode():

    styleCodes = load_workbook(filename="StyleCodes.xlsx")
    sheet = styleCodes.active
    print(sheet)

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
