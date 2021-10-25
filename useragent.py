from fake_useragent import UserAgent
import requests

def ua():

    ua = UserAgent()
    return ua.chrome

print(ua())
# <div class="chakra-container css-vp2g1e" data-component="ProductView">
