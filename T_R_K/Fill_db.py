import sqlite3

dblink = sqlite3.connect("catalog.db")
dbutcher = dblink.cursor()

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
        dbutcher.execute("INSERT INTO Catalog(title, description, price, tglink, mediatype) VALUES (?,?,?,?,?)",
                         (title,description, price, tglink, mediatype))
        dblink.commit()


    dblink.close()
