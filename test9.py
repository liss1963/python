import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Liss1963',
    database='test'
)
df = pd.read_sql_query("SELECT * FROM hospital", mydb)
print(df)
df1 = df['Hospital_Id']
for num in range(len(df1)):
    if df1.loc[[num][0]] == 2:
        a = num
print(df.iloc[a])
