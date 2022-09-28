import requests
from bs4 import BeautifulSoup

output_file = open('quotes.txt', 'w')

res = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(res.text, 'lxml')

quotes = soup.find_all('div', {'class':'quote'})
# quotes = soup.find_all('span', {'class':"text"})

# print(type(quotes))
# print(quotes)

for quote_data in quotes:
    quote = quote_data.find('span', {'class':'text'})
    # print(quote.text)
    output_file.write(quote.text + '\n')