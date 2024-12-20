from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from T_R_K.Fill_db import dblink, dbutcher


dbutcher.execute("SELECT * FROM Catalog")
all_rows = dbutcher.fetchall()

column_names = [description[0] for description in dbutcher.description]

if all_rows:
    buttons = []
    call_data = []
    for row in all_rows:
        buttons.append(f"{row[1]}, Цена {row[3]}р.")
        call_data.append(f"product_buying{row[0]}")
    buttons.append("Назад")
    call_data.append("back_to_main")
else:
    buttons = ["Нет товаров в наличии."]
    call_data = ["back_to_main"]

kb_buttons = [[InlineKeyboardButton(text=text, callback_data=callback)]
              for text, callback in zip(buttons, call_data)]
kb_catalog = InlineKeyboardMarkup(inline_keyboard=kb_buttons)



