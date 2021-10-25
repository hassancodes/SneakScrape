from fake_useragent import UserAgent
import requests

def ua():

    ua = UserAgent()
    return ua.chrome

print(ua())
