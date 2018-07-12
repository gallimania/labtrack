# This file is responsible for providing the main program with the ability to execute SQL commands 
# and allow the program to store and retrieve data from the database file.

import sqlite3 as sql3

sql_conn = sql3.connect('inventory.db')
sql_curs = sql_conn.cursor()

def create_table(entry_tableName):
  ''' Creates a table within the created database file using the table name specified by the
  variable entry_tableName '''
  sql_command = '''CREATE TABLE {} (TEXT, cas_num TEXT, purchase_price TEXT, purchase_amt TEXT)
  INSERT (?,?,?,?)'''.format(entry_tableName)
  sql_curs.execute(sql_command)

def new_entry(chemical_name, cas_num, purchase_price, purchase_amt):
  ''' Function that inserts a new row of data into the specified table. '''
  sql_curs.execute('''
  INSERT INTO chemicals VALUES ({},{},{},{})
  ''').format(chemical_name, cas_num, purchase_price, purchase_amt)
  
