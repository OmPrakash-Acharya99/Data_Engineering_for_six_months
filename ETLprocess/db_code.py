import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names=attribute_list)
df.to_sql(table_name, conn, if_exists='replace', index=False)
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_appendd = pd.DataFrame(data_dict)   
data_appendd.to_sql(table_name,conn,if_exists = 'append', index = False)
print('Data appended successfully')
conn.close()