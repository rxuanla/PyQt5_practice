import sqlite3

conn = sqlite3.connect('testingDB.db')

try:
    cur = conn.cursor()
    account = 'test001'
    cur.execute(
        "SELECT * FROM member where account =?", (account,))
    for row in cur:
        print(row)
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])
