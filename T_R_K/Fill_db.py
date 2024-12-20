#Fill_db.py

import sqlite3


dblink = sqlite3.connect("DataBases/catalog.db")
dbutcher = dblink.cursor()

def db_commit():
    global dblink
    dblink.commit()
    return

def db_add_user(username, email, age, balance,tgid):
    global dblink, dbutcher
    dbutcher.execute("INSERT INTO Users(username, email, age, balance, tgid)"
                     " VALUES (?,?,?,?,?)",
                     (username, email, age, balance, tgid))
    dblink.commit()
    return

def db_user_is_included(username):
    global dblink, dbutcher
    dbutcher.execute("SELECT EXISTS (SELECT 1 FROM Users WHERE username = ?)", (username,))
    result = dbutcher.fetchone()[0]
    return bool(result)

def db_close():
    global dblink
    dblink.close()
    return

if __name__ == "__main__" :
    dbutcher.execute('''
    CREATE TABLE IF NOT EXISTS Catalog(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    tglink TEXT,
    mediatype TEXT
    )
    ''')

    k = int(input("Сколько товаров добавим?"))
    for i in range(k):
        title = input("Название TEXT:")
        description = input("Описание TEXT:")
        price = input("Цена INTEGER NOT NULL:")
        tglink = input("Телеграмм ссылка TEXT:")
        mediatype = input("video, audio, voice, photo, text:")
        dbutcher.execute("INSERT INTO Catalog(title, description, price, tglink, mediatype)"
                         " VALUES (?,?,?,?,?)",
                         (title,description, price, tglink, mediatype))
        dblink.commit()


    dbutcher.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT,
        age INTEGER NOT NULL,
        balance INTEGER,
        tgid INTEGER
        )
        ''')
    dblink.commit()

    dblink.close()
