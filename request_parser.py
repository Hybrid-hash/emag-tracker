import requests
import time
from numberspy import parseNumber
from bs4 import BeautifulSoup


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
        #print(f'{product_name},{newprice_value},{time_day},{time_clk}')
        
        with open('data.csv','a') as f:
            f.write(str(product_name) + ','+ str(newprice_value)+ '\n')

def print_current_price():
    total=0.0
    with open('urls.txt') as f:
        my_list2=f.read().splitlines()
        for url in my_list2:
            response= requests.get(url)
            soup = BeautifulSoup(response.text,'html.parser')
            product_name=soup.find('title').text
            newprice_str=soup.find('p', class_='product-new-price').text.strip().replace('Lei','')
            newprice_str2=newprice_str[:-3]+',99'
            newprice_value= parseNumber(newprice_str2)
            time_day= time.strftime("%Y/%m/%d")
            time_clk= time.strftime("%H:%M")
            total = total + float(newprice_value)
            #print(f'{product_name:><50},{newprice_value},{time_day},{time_clk}')
            print(f"{product_name:<120}{newprice_value:<10}{time_day} {time_clk}")
    print(f'Total price is {total:.2f}')