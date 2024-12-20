import sqlite3
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)


dblink = sqlite3.connect("T_R_K.DataBases.catalog.db")
dbutcher = dblink.cursor()

dbutcher.execute("SELECT * FROM Catalog")
all_rows = dbutcher.fetchall()

column_names = [description[0] for description in dbutcher.description]

if all_rows:
    buttons = []
    call_data = []
    for row in all_rows:
        buttons.append(f"{row[1]}, Цена {row}р.")
        call_data.append(f"product_buying{row[0]}")
else:
    buttons = ["Нет товаров в наличии."]
    call_data = ["back_to_main"]


kb_buttons = [[InlineKeyboardButton(text, callback)] for text, callback in zip(buttons, call_data)]



abc = [[InlineKeyboardButton(text="Новость Цена 100р.", callback_data="product_buying1")],
    [InlineKeyboardButton(text="Музон Цена 200р.", callback_data="product_buying2")],
    [InlineKeyboardButton(text="Урок по шахматам Цена 300р.", callback_data="product_buying3")],
    [InlineKeyboardButton(text="Блокбастер Цена 400р.", callback_data="product_buying4")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_main")]]

kb_catalog = InlineKeyboardMarkup(inline_keyboard=kb_buttons)

dblink.close()

