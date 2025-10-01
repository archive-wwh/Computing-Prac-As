#using python (application) with built in sqlite3 module (connector) to interact with sqlite databases
#syntax for insert different from sql but others same

'''
structure of sqlite code for a levels h2 computing:

import sqlite3
connection = sqlite3.connect("database.db")
connection.execute("sql statement")
connection.commit()
connection.close()

special things:
cursor after execute SELECT command to use python to manipulate data from database

rollback before commit
'''


import sqlite3 #import required module



#connect function allows usage of python to operate sql codes

'''
accepts a string argument, which consists of path and full name of database file, with file extension (.db)

sqlite database assumed to be in same directory as python file if no path is provided (most common as convenient for testing)
empty database with given name will be created if specified file does not exist
'''

connection = sqlite3.connect("path_name/name_of_database.db") 



#execute method contains sql statement (refer to sql notes)

'''
recommend to create table in db browser for sqlite then copy the CREATE TABLE statement
such practice prevents errors from wrong syntax

presence of foreign keys
IF foreign key constraints are enforced

insert into table without foreign key first (referrenced by foreign key)

order opposite for delete; delete table with foreign key first

"" for sql statement to be one line however
''' ''' is the more common practice as it allows sql statement to span multiple lines, improving readibility
'''

#sql in one line
connection.execute("SELECT column_name FROM table_name WHERE column_name = 'data' ")

#sql over multiple lines
connection.execute('''
SELECT column_name
FROM table_name
WHERE column_name = 'data' ''')


'''
using place holder

maintains data integrity as opposed to direct string concatenation to sql command
prevents misinterpretation of data, which can corrupt database

? acts as placeholder
uses a tuple to store needed data then replace placeholder with respective data
parameter substitution follows sql's order (first value in tuple for first placeholder, etc)
 
difference in syntax from sql:

, (tuple) after quotes but inside execute brackets
IMPORTANT: for one column insertion, (item,) NOT (item) to create a tuple
'''

#delete using placeholder for one column
connection.execute('''
DELETE FROM table_name
column_name = ? ''',(data,))

#insert using placeholder for multiple columns
connection.execute('''
INSERT INTO table_name(column1_name, column2_name, column3_name)
VALUES (?,?,?) ''',(data1, data2, data3))


#cursor object

'''
used to deal with data from execute SELECT commands

cursor contains rows of tuples
'''

#create cursor

cursor = connecton.execute('''
SELECT column1_name, column2_name, column3_name
FROM table_name
WHERE column4_name = ? ''',(data,))


#fetchone method

#returns current row as a tuple then advance to next row
#will be the first row if nothing has been done to cursor

a_row_of_data = cursor.fetchone()  


#fetchall method

#returns list of tuples (something like a 2d array)

all_data = cursor.fetchall()

for row in all_data: #iterate through list; standard
    print(f"{column2_name} is {row[1]}")
    #position of each value in tuple is dependent on position of column in SELECT command
    #first column in SELECT will be index zero of tuple; first item, etc

    #if tuple only has one item
    #print(row[0]) as first item of tuple is the desired element


    
#commit method

'''
IMPORTANT: RESPONSIBLE FOR MAJORITY OF CASES WHERE CHANGE IS NOT REFLECTED PROPERLY IN DB BROWSER FOR SQLITE
similar to clicking write changes in db browser for sqlite, enables modifications to data to be saved
in other words, need commit for all sql statements, which involves changes to database, everything except SELECT

best to have commit after every execute for debugging purpose as can check db browser for sqlite for which execute failed
'''

connection.commit()



#close method

'''
ensures proper closure of database
prevents locking of database, which happens when a open connection to databse exists
'''

connection.close()
 



#rollback method

'''
not very useful personally cause can always delete database and modify the wrong codes

used to discard modifications to data during current transaction (before last commit)
commands that deal with the database's structure (CREATE, etc) will not be reversed as they do not open a transaction
'''

connection.rollback()

