# pip install mysql-connector-python
#PES1UG20CS262
#NAYAN JAIN
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
c = mydb.cursor()


#def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
#              'dealer_street TEXT)')


def add_data(Seller_id,s_pass,Name,Address):
    c.execute('INSERT INTO Seller(Seller_id,s_pass,Name,Address) VALUES (%s,%s,%s,%s)',
              (Seller_id,s_pass,Name,Address))
    mydb.commit()


def pro_add_data(Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id):
    c.execute('INSERT INTO product(Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM Seller')
    data = c.fetchall()
    return data


def cus_view_all_data():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data


def pay_view_all_data():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data


def pro_view_all_data():
    c.execute('SELECT * FROM product')
    data = c.fetchall()
    return data


def view_only_seller_names():
    c.execute('SELECT Name FROM Seller')
    data = c.fetchall()
    return data


def view_only_customer_names():
    c.execute('SELECT Name FROM customer')
    data = c.fetchall()
    return data


def view_only_product_names():
    c.execute('SELECT Product_id FROM product')
    data = c.fetchall()
    return data


def get_seller(Name):
    c.execute('SELECT * FROM Seller WHERE Name="{}"'.format(Name))
    data = c.fetchall()
    return data


def get_customer(Name):
    c.execute('SELECT * FROM customer WHERE Name="{}"'.format(Name))
    data = c.fetchall()
    return data


def get_product(Product_id):
    c.execute('SELECT * FROM product WHERE product_id="{}"'.format(Product_id))
    data = c.fetchall()
    return data


def edit_seller_data(new_Seller_id,new_s_pass,new_Name,new_Address,Seller_id,s_pass,Name,Address):
    c.execute("UPDATE Seller SET Seller_id=%s, s_pass=%s, Name=%s, Address=%s WHERE "
              "Seller_id=%s and s_pass=%s and Name=%s and Address=%s", (new_Seller_id,new_s_pass,new_Name,new_Address, Seller_id,s_pass,Name,Address))
    mydb.commit()
    data = c.fetchall()
    return data


def edit_customer_data(new_Customer_id,new_c_pass,new_Name,new_Address,new_Pincode,new_Phone_number_s,new_cart_id,Customer_id,c_pass,Name,Address,Pincode,Phone_number_s,cart_id):
    c.execute("UPDATE customer SET Customer_id=%s, c_pass=%s, Name=%s, Address=%s, Pincode=%s, Phone_number_s=%s, cart_id=%s WHERE "
              "Customer_id=%s and c_pass=%s and Name=%s and Address=%s and Pincode=%s and Phone_number_s=%s and cart_id=%s", (new_Customer_id,new_c_pass,new_Name,new_Address,new_Pincode,new_Phone_number_s,new_cart_id,Customer_id,c_pass,Name,Address,Pincode,Phone_number_s,cart_id))
    mydb.commit()
    data = c.fetchall()
    return data


def edit_product_data(new_Product_id,new_Type,new_Color,new_P_Size,new_Gender,new_Commission,new_Cost,new_Quantity,new_Seller_id,Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id):
    c.execute("UPDATE product SET Product_id=%s, Type=%s, Color=%s, P_Size=%s, Gender=%s, Commission=%s, Cost=%s, Quantity=%s, Seller_id=%s WHERE "
              "Product_id=%s and Type=%s and Color=%s and P_Size=%s and Gender=%s and Commission=%s and Cost=%s and Quantity=%s and Seller_id-%s", (new_Product_id,new_Type,new_Color,new_P_Size,new_Gender,new_Commission,new_Cost,new_Quantity,new_Seller_id,Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(Name):
    c.execute('DELETE FROM Seller WHERE Name="{}"'.format(Name))
    mydb.commit()


def cus_delete_data(Name):
    c.execute('DELETE FROM customer WHERE Name="{}"'.format(Name))
    mydb.commit()


def pro_delete_data(Product_id):
    c.execute('DELETE FROM product WHERE Name="{}"'.format(Product_id))
    mydb.commit()

def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data

