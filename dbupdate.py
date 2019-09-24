import requests
import time
from numberspy import parseNumber
from bs4 import BeautifulSoup
import hashlib
import database_manager as db_updater 


with open('urls.txt') as f:
    my_list=f.read().splitlines()
    for url in my_list:
        response= requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        product_name=soup.find('title').text
        newprice_str=soup.find('p', class_='product-new-price').text.strip().replace('Lei','')
        newprice_str2=newprice_str[:-3]+',99'
        newprice_value= parseNumber(newprice_str2)
        time_day= time.strftime("%Y/%m/%d")
        time_clk= time.strftime("%H:%M")
        db_updater.update_database(url,float(newprice_value),time_day,time_clk,product_name)

