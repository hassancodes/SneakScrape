import json
import requests

url = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/product_variants_v2/query?x-algolia-agent=Algolia for vanilla JavaScript 3.25.1&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a'
data = {"params":"distinct=true&facetFilters=()&facets=%5B%22size%22%5D&hitsPerPage=20&numericFilters=%5B%5D&page=0&query="}
r = requests.post(url, data=json.dumps(data))
print(r.json()['hits'][0])
