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
