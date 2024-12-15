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
    [InlineKeyboardButton(text="Продукт 1", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 2", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 3", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")]
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