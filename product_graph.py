import sqlite3
import hashlib 

def display_graph(url_index):
    connection =sqlite3.connect('track.db')
    cursor = connection.cursor()
    with open('urls.txt') as f:
        my_list=f.read().splitlines()
        url = my_list[url_index]
        result = hashlib.md5(url.encode())
        result_hex= result.hexdigest()
        sql_search = 'select * from products_price where id_product = ?;'
        cursor.execute(sql_search, (result_hex,))
        product_list=cursor.fetchall()
        print(url)
        for row in product_list:
            print(f'{row[2]} {row[3]}{row[4]}')
            #print(product_list[0][3])
            #print(product_list[1][3])
        #for url in my_list:           
            #print(url)
            #print('\n')

#https://www.daniweb.com/programming/software-development/threads/482270/plot-date-and-time-xaxis-versus-a-value-yaxis-using-data-from-txt-file
        