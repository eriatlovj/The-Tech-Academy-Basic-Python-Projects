import sqlite3

conn = sqlite3.connect("test3.db")

cur = conn.cursor()
with conn:
    cur.execute("CREATE TABLE IF NOT EXISTS files (ID INTEGER PRIMARY KEY AUTOINCREMENT,file_name TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect("test3.db")
cur = conn.cursor()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

insert = 'INSERT INTO files (file_name) VALUES (?)'

for file in fileList:
    if file.endswith(".txt"):
        cur.execute(insert,[file])
        conn.commit()

cur.execute("SELECT file_name FROM files")

result = cur.fetchall()

for value in result:
    msg = "File Name: {}".format(value[0])
    print(msg)
