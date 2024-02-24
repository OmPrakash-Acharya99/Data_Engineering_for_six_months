import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')
table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']
file_path = '/home/project/Data_Engineering_for_six_months/ETLprocess/ETLexercise/Departments.csv'

df = pd.read_csv(file_path, names=attribute_list)
df.to_sql(table_name, conn, if_exists='replace', index=False)
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ["L0010"],
            }
data_appendd = pd.DataFrame(data_dict)   
final_data = data_appendd.to_sql(table_name,conn,if_exists = 'append', index = False)
print('Data appended successfully')
query_statement = f"SELECT * FROM {table_name}"
table_data = pd.read_sql(query_statement, conn)
print(table_data)