import psycopg2

def insert_sales(conn, order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount !=0:
        order_total = order_total * discount
    sale_data = (order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount, order_total)
    cur = conn.cursor()
    cur.execute(''' INSERT INTO SALES(order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount, order_total) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s)
    ''', sale_data)
    conn.commit()
        
    cur.execute(''' DELETE FROM SALES WHERE order_num=1105910''')

    rows = cur.fetchall()
    for row in rows:
        print(rows)
        print("CUST_NAME=", row[0])
        print("ORDER_TOTAL=", row[1], "\n")

if __name__ == '__main__':
    conn = psycopg2.connect(database="red30",
        user="postgres",
        password="smith3dx",
        host="localhost",
        port="5432")

    order_num = int(input("what is the order number?\n"))
    order_type = input("what is the order typer: Retail or wholesale?\n")
    cust_name = input("what is the customer name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("what is the product name?\n")
    quantity = float(input("how many were brought?\n"))
    price = float(input("what is the price of the product?\n"))
    discount = float(input("what is discount, if there is one?\n"))

    insert_sales(conn, order_num, order_type, cust_name, prod_name, prod_number, quantity, price, discount)
 
    order_num = int()

    conn.cursor()

# cursor.execute("SELECT * FROM SALES LIMIT 10")
# print(cursor.fetchall())

# cursor.execute('''INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) 
#                 VALUES(1105911, 'Ratail', 'Syman Mapstone', 'EB521', 'Understanding AI', 3, 19.5, 0, 58.5) ''')


#conn.commit()

#cursor.execute("SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=1105911")


    order_num = int(input("what is the order number?\n"))
    

conn.close()
 