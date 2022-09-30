import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.flipkart.com/dreamcase-back-cover-vivo-v3/p/itmfdthznwxdrghf?pid=ACCFDTHH2EZFGDHW&lid=LSTACCFDTHH2EZFGDHWAWM7OY&marketplace=FLIPKART&q=vivo+v3+back+cover&store=tyy%2F4mr%2Fq2u&srno=s_1_30&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&fm=organic&iid=d5f5f353-f1d3-4d82-9881-b71391fd33f8.ACCFDTHH2EZFGDHW.SEARCH&ppt=hp&ppn=homepage&ssid=jh49e16sls0000001664535567419&qH=ed1eeb365b28deb4')
soup = BeautifulSoup(res.text, 'lxml')

price_value = soup.find('div', {'class':'_30jeq3 _16Jk6d'}).text
# print(price_value)

price = float(price_value[1:])

if price <= 100:
    print('Buy it now', price_value)
else:
    print('Price is not low', price_value)