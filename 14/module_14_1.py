import sqlite3
import Fake_person

dblink = sqlite3.connect("not_telegram.db")
dbutcher = dblink.cursor()


dbutcher.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    person = Fake_person.faker_person_create()
    dbutcher.execute("INSERT INTO Users(username, email, age, balance) VALUES (?,?,?,?)",
                     (person["Ф.И.О."],person["E-mail"], int(person["Возраст"]), 1000,))
dblink.commit()


dbutcher.execute("PRAGMA table_info(Users)")
num_columns = len(dbutcher.fetchall())

#dbutcher.execute("UPDATE Users SET balance=500 WHERE id%2=1") #упрощенные махинации с балансом.
dbutcher.execute("SELECT id FROM Users")  # махинации с балансом
rows = dbutcher.fetchall()
for i, row in enumerate(rows):
    if (i + 1) % 2 == 1:
        dbutcher.execute("UPDATE Users SET balance = 500 WHERE id = ?", (row[0],))
        dblink.commit()

#сокращение штата, обьемы упали
dbutcher.execute("SELECT id FROM Users")
rows = dbutcher.fetchall()
for i, row in enumerate(rows):
    if i % 3 == 0:
        dbutcher.execute("DELETE FROM Users WHERE id = ?", (row[0],))
        dblink.commit()


dbutcher.execute("SELECT * FROM Users WHERE age!=60")# 60 лет!
all_rows = dbutcher.fetchall()

column_names = [description[0] for description in dbutcher.description]

if all_rows:
    for row in all_rows:
        for col_name, value in zip(column_names[1:], row[1:]):
            print(f"{col_name}:{value} | ", end="")
        print()
else:
    print("Запрос не вернул результатов.")


dblink.commit()
dblink.close()

