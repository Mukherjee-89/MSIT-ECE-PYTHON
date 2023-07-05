import mysql.connector
name=str(input("enter name of customer table :"))
address=str(input("enter adress of customer table :"))
name_1=str(input("enter name of customers_1 table :"))
address_2=str(input("enter adress of customers_1 table :"))
email=str(input("enter email of customers_1 table :"))
gender=str(input("enter gender of customers_1 table :"))
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit_ece"
)
mycursor=db.cursor()
sql="INSERT INTO customers(name,address)VALUES(%s,%s)"
val=(name,address)
mycursor.execute(sql,val)
sql_2="INSERT INTO customers_1(name,address,email,gender)VALUES(%s,%s,%s,%s)"
val_2=(name_1,address_2,email,gender)
mycursor.execute(sql_2,val_2)
db.commit()
print(mycursor.rowcount,"record inserted")