#go to ebay.com and search a random item and download first 10 pages of search results
#create a dictionary with name of the item, status of the item (brand new, refrubished, pre-owned), and price and create a json 
#file of that dictionary 
#upload repository and read.me file

import requests 
#import time
#import bs4
from bs4 import BeautifulSoup 

keyword = 'camera'
page_number = '1'
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0'
}

for i in range(1,11):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i), headers=headers)
    print('r.status_code=', r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')
    #print('r.text=', r.text)

    """
    #Extracting titles (names) of the items 
    items = soup.select('.s-item__title')
    for item in items:
        print('item =',item.text)

    #Extracting prices of the items 
    #ask question about the ones with bid prices 
    prices = soup.select('.s-item__price')
    for price in prices:
        print('Price = ', price.text)

    #Extracting condition of each item 
    conditions = soup.select('.SECONDARY_INFO')
    for condition in conditions:
        print('Condition = ', condition.text)

    """
    #new_list = []
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        #print('- - -')
        result = {}
        titles = box.select('.s-item__title')
        for title in titles:
            #print('title =',title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price = ', price.text)
            result['price'] = price.text 
        conditions = box.select('.SECONDARY_INFO')
        for condition in conditions:
            #print('Condition = ', condition.text)
            result['condition'] = condition.text
        #print('result=',result)
        results.append(result)

    print('len(results)=', len(results))

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
#print('j =',j)