#! /usr/bin/env python3

#installing all used packages
    #source: https://stackoverflow.com/questions/17271444/how-to-install-a-missing-python-package-from-inside-the-script-that-needs-it

import sys, csv, psycopg2


db_host = sys.argv[-5]
db_port = sys.argv[-4]
db_name = sys.argv[-3]
db_user = sys.argv[-2]
db_password = sys.argv[-1]

#names of the csv files which contain the data
confs_csv_name = sys.argv[1]#'confs.csv'
journals_csv_name = sys.argv[2]#'journals.csv'
persons_csv_name = sys.argv[3]#'persons.csv'
pubs_csv_name = sys.argv[4]#'pubs.csv'
theses_csv_name = sys.argv[5]#'theses.csv'

#------------------------------------------------------------------------------------------------------------------------------------------

#HELP:
'''
---Insertion to database:
   cur.execute('INSERT INTO Table1 (col1, col2) VALUES(%s, %s)', (value1, value2))

---Fetching from database:-----------------------------------------------------------------------------------------------------------------
   cur.execute(query)
   resultSet = cur.fetchall() - to fetch the whole result set
   reultSet = cur.fetchone() - to fetch a single row(does not mean only the first row, it means one row at a time)
-------------------------------------------------------------------------------------------------------------------------------------------
'''


def csv_to_list(csv_name):
#gets data from the csv file and puts it into a list of lists
#for accessing the data: data_list[row_number][column_number]
    data_list = []
    with open(csv_name, 'r', encoding='utf-8') as csvfile:
      data_squads = csv.reader(csvfile)
      
      for row in data_squads:
        #to remove all the ', to have no collisions in the code later on
        new_row = []
        for element in row:
          if isinstance(element, str):
            element = element.replace("'", "`")
          new_row.append(element)
        #print(new_row)
            
        data_list.append(new_row)
      #deletes the fist row, which contains the table heads
      #optional:uncomment if this makes working with the data easier for you
      #del data_list[0]
    return data_list

def semicolon_string_to_list(string):
#interprets all ; of the given string as separator of elements
#returns a list of strings
    return string.split(';')

#------------------------------------------------------------------------------------------------------------------------------------------

#Lists from csvs
confs_list = csv_to_list(confs_csv_name)
journals_list = csv_to_list(journals_csv_name)
persons_list = csv_to_list(persons_csv_name)
pubs_list = csv_to_list(pubs_csv_name)
theses_list = csv_to_list(theses_csv_name)


#SQL connection
sql_con = psycopg2.connect(host = db_host, port = db_port, database = db_name, user = db_user, password = db_password)
#cursor, for DB operations
cur = sql_con.cursor()

#commit the changes, this makes the database persistent
sql_con.commit()

#close connections
cur.close()
sql_con.close()
