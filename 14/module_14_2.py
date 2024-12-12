import sqlite3

dblink = sqlite3.connect("not_telegram.db")
dbutcher = dblink.cursor()

# delId = int(input('\n Введите id пользователя для удаления\n>>>:'))
dellId = 6
dbutcher.execute(f"DELETE FROM Users WHERE id = {dellId}")
dblink.commit()


dbutcher.execute("SELECT balance FROM Users")
rows = dbutcher.fetchall()

num_rows = len(rows) + 1
balanceTotal = sum(row[0] for row in rows)

averageBalance = balanceTotal/num_rows

print(f"{averageBalance:.2f}")
dblink.close()
