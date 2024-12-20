from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)




kb_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчет калорий", callback_data="calories_math")],
    [InlineKeyboardButton(text="Помощь", callback_data="help")],
    [InlineKeyboardButton(text="Приветствие", callback_data="hello")],
    [InlineKeyboardButton(text="Иформация", callback_data="info")],
    [InlineKeyboardButton(text="Каталог", callback_data="buy_menu")]
])

kb_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новость Цена 100р.", callback_data="product_buying1")],
    [InlineKeyboardButton(text="Музон Цена 200р.", callback_data="product_buying2")],
    [InlineKeyboardButton(text="Урок по шахматам Цена 300р.", callback_data="product_buying3")],
    [InlineKeyboardButton(text="Блокбастер Цена 400р.", callback_data="product_buying4")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_main")]
])

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder="Воспользуйтесь кнопками ниже." )