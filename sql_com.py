# This file is responsible for providing the main program with the ability to execute SQL commands 
# and allow the program to store and retrieve data from the database file.

import sqlite3 as sql3

sql_conn = sql3.connect('inventory.db')
sql_curs = sql_conn.cursor()

def create_table():
  sql_curs.execute("
  CREATE TABLE chemicals(chemical_name TEXT, cas_num TEXT, purchase_price TEXT, purchase_amt TEXT
  ")
