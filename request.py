import requests

from numberspy import parseNumber
from bs4 import BeautifulSoup






with open('urls.txt') as f:
    my_list2=f.read().splitlines()
    for url in my_list2:
        response= requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(response.text,'html.parser')
        product_name=soup.find('title').text
        newprice_str=soup.find('p', class_='product-new-price').text.strip().replace('Lei','')
        newprice_str2=newprice_str[:-3]+',99'
        newprice_value= parseNumber(newprice_str2)
        print(f'{product_name},{newprice_value}')
        #with open('original.csv','a') as f:
         #   f.write(str(product_name) + ';'+ str(date) + ';' + str(newprice_value)+ '\n')
