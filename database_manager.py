import sqlite3
import hashlib 
def create_database():
    connection =sqlite3.connect('track.db')

    cursor = connection.cursor()

    sql = """ 
            CREATE TABLE IF NOT EXISTS products(
                id VARCHAR(128) PRIMARY KEY,
                name VARCHAR(256)
            );
    """
    cursor.execute(sql)
    sql2= """ 
            CREATE TABLE IF NOT EXISTS products_price(
                id_value INTEGER PRIMARY KEY,
                id_product VARCHAR(128),
                price FLOAT,
                date VARCHAR(12),
                time VARCHAR(6),
                FOREIGN KEY (id_product) REFERENCES products (id)
            );
            """
    cursor.execute(sql2)
    connection.commit()
    connection.close()

def update_database(url,price,date,time):
    connection =sqlite3.connect('track.db')
    cursor = connection.cursor()
    result = hashlib.md5(url.encode())
    result_hex= result.hexdigest()
    #print(f'Hash is {result_hex}')
    record_name = [result_hex, url]
    record_value = [result_hex, price, date, time]
    # cursor.execute('insert into products values (?,?)',(result.hexdigest()),url)
    # cursor.execute('insert into products_price values (?,?,?,?,?)',1,result,price,date,time)
    #c.execute('insert into tablename values (?,?,?)', item)
    # sqlproduct = 'insert into products(id,name) values (?,?);'
    # cursor.execute(sqlproduct, record_name)
    # sqlproductvalue = 'insert into products_price(id_product,price,date,time) values (?,?,?,?,?);'
    # cursor.execute(sqlproductvalue, record_value)

    #cursor.execute(f'INSERT INTO products VALUES ("{record_name[0]}","{record_name[1]}")')
    cursor.execute(f'INSERT INTO products_price (id_product,price,date,time) VALUES ("{record_value[0]}","{record_value[1]}","{record_value[2]}","{record_value[3]}")')
    connection.commit()
    connection.close()

# #cursor.execute(sql3)
# cursor.execute(sql4)


# sql3 = """
# INSERT INTO products VALUES (10, "New product");
# """

# sql4 = """
# INSERT INTO products_price(id_product, price,date,time) VALUES (10, 450.9, "19/09/2019", "12:00");
# """
# CREATE TABLE IF NOT EXISTS projects (
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     begin_date text,
#     end_date text
# );

# CREATE TABLE IF NOT EXISTS tasks (
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     priority integer,
#     project_id integer NOT NULL,
#     status_id integer NOT NULL,
#     begin_date text NOT NULL,
#     end_date text NOT NULL,
#     FOREIGN KEY (project_id) REFERENCES projects (id)
# );

# record = (10, 'Leonardo Romano', 'Marketing', '+40122111', 'leo@x.com')
 
# ## Creating the sql statement. Each ? will be replaces with an item of the tuple
# sql = 'insert into employees values (?,?,?,?,?);'
#cursor.execute(sql, record)