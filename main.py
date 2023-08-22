import os
import mysql.connector
import datetime

now = datetime.datetime.now()


def product_mgmt():
    while True:
        print("\t\t\t 1. Add New Product")
    print("\t\t\t 2. List Product")
    print("\t\t\t 3. Update Product")
    print("\t\t\t 4. Delete Product")
    print("\t\t\t 5. Back (Main Menu)")
    p = int(input("\t\tEnter Your Choice :"))
    if p == 1:
        add_product()
    if p == 2:
        search_product()
    if p == 3:
        update_product()
    if p == 4:
        delete_product()
    if p == 5:
        break


def purchase_mgmt():
    while True:
        print("\t\t\t 1. Add Order")
    print("\t\t\t 2. List Order")
    print("\t\t\t 3. Back (Main Menu)")
    o = int(input("\t\tEnter Your Choice :"))
    if o == 1:
        add_order()
    if o == 2:
        list_order()
    if o == 3:
        break


def sales_mgmt():
    while True:
        print("\t\t\t 1. Sale Items")
    print("\t\t\t 2. List Sales")
    print("\t\t\t 3. Back (Main Menu)")
    s = int(input("\t\tEnter Your Choice :"))
    if s == 1:
        sale_product()
    if s == 2:
        list_sale()
    if s == 3:
        break


def sales_mgmt():
    while True:
        print("\t\t\t 1. Sale Items")
    print("\t\t\t 2. List Sales")
    print("\t\t\t 3. Back (Main Menu)")
    s = int(input("\t\tEnter Your Choice :"))
    if s == 1:
        sale_product()
    if s == 2:
        list_sale()
    if s == 3:
        break


def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="aparnamohan@123", port=3306)
    mycursor = mydb.cursor()
    print(" Creating PRODUCT table")
    sql = "CREATE TABLE if not exists product (\
 pcode int(4) PRIMARY KEY,\
 pname char(30) NOT NULL,\
 pprice float(8,2) ,\
 pqty int(4) ,\
 pcat char(30));"


mycursor.execute(sql)
print(" Creating ORDER table")
sql = "CREATE TABLE if not exists orders (\
 orderid int(4)PRIMARY KEY ,\
 orderdate DATE ,\
 pcode char(30) NOT NULL , \
 pprice float(8,2) ,\
 pqty int(4) ,\
 supplier char(50),\
 pcat char(30));"
mycursor.execute(sql)
print(" ORDER table created")
print(" Creating SALES table")
sql = "CREATE TABLE if not exists sales (\
 salesid int(4) PRIMARY KEY ,\
 salesdate DATE ,\
 pcode char(30) references product(pcode), \
 pprice float(8,2) ,\
 pqty int(4) ,\
 Total double(8,2)\
 );"
mycursor.execute(sql)
print(" SALES table created")
sql = "CREATE TABLE if not exists user (\
 uid char(6) PRIMARY KEY,\
 uname char(30) NOT NULL,\
 upwd char(30));"
mycursor.execute(sql)
print(" USER table created")
