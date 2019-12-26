'''
Created on Dec 23, 2019

@author: sedlmeier
'''
import mysql.connector


print("AUTODB!")

def connect():
    mydb = mysql.connector.connect(
        host = "qnas",
        port=33061,
        user = "root",
        password = "apollo",
        database = "autodb"
    )
    return mydb

def create_autodb():
    mydb = connect()    
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE DATABASE autodb")
    except Exception as ex:
        print ("autodb alread exists or could not be created")        
    mycursor.execute("SHOW DATABASES")    
    for x in mycursor:
        print(x)


def create_table_brands():
    mydb = connect()    
    mycursor = mydb.cursor()    
    mycursor.execute("CREATE TABLE brands (id, AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255), foundationYear VARCHAR(10)")    
    mycursor.execute("SHOW TABLES")    
    for x in mycursor:
        print(x)
    
    #mycursor.execute("ALTER TABLE brands ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

def insert_brands():
    mydb = connect()    
    mycursor = mydb.cursor()
    sql = "INSERT INTO brands (name, country, foundationYear) VALUES (%s, %s, %s)"
    val = [('BMW', 'Deutschland', '1916'),
           ('Mercedes', 'Deutschland', '1926'),
           ('Audi', 'Deutschland', '1910'),
           ('Volkswagen', 'Deutschland', '1937'),
           ('Porsche', 'Deutschland', '1931'),
           ('Artega', 'Deutschland', '2006'),
           ('Gumpert', 'Deutschland', '2004'),
           ('Borgward', 'Deutschland', '1939'),
           ('AC Automitive GMBH', 'Deutschland', '2009'),
           ('Bitter', 'Deutschland', '1971'),
           ('CN Fahrzeugbau', 'Deutschland', '1986'),
           ('e.GO', 'Deutschland', '2015'),
           ('Ford', 'Deutschland/Grossbritannien/USA', '1903'),
           ('German E-Cars', 'Deutschland', '2009'),
           ('HKT', 'Deutschland', '1983'),
           ('Isdera', 'Deutschland', '1982'),
           ('Jetcar', 'Deutschland', '2000'),
           ('Karabag', 'Deutschland', '1992'),
           ('Lotec', 'Deutschland', '1962'),
           ('Opel', 'Deutschland', '1962'),
           ('Roding', 'Deutschland', '2008'),
           ('Rudolph Perfect Roadster', 'Deutschland', '1992'),
           ('Ruf', 'Deutschland', '1939'),
           ('Rush', 'Deutschland', '2000'),
           ('Smart', 'Deutschland', '1994'),
           ('Streetscooter', 'Deutschland', '2010'),
           ('Weineck', 'Deutschland', '2000'),
           ('YES', 'Deutschland', '1998'),
           ('9FF', 'Deutschland', '2001')
    ]
    mycursor.executemany(sql, val)    
    mydb.commit()
    print(mycursor.rowcount, "was inserted")