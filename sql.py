import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""
cursor.execute(table_info)


#insert some records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',75)''')
cursor.execute('''Insert Into STUDENT values('Rohit','Data Science','A',84)''')
cursor.execute('''Insert Into STUDENT values('Vikash','Devops','A',65)''')
cursor.execute('''Insert Into STUDENT values('Anita','Devops','A',79)''')

print("The inserted records are: ")
data = cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
