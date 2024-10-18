from telebot import types


def menu_button():
    btn1 = types.KeyboardButton(text='Получить все заявки')
    btn2 = types.KeyboardButton(text='Получить заявку по ID')
    btn3 = types.KeyboardButton(text='Обновить заявку')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn1, btn2)
    markup.row(btn3)

    return markup
