import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="test", password="test", database="python_simple"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM tasks")

result = cursor.fetchall()

for row in result:
    print(row)

# Let's insert a row
task = input("Type a new task: ")
sql = "INSERT INTO tasks (task) VALUES (%s)"
data = (task,)
cursor.execute(sql, data)
db.commit()