from telebot import types

buttons = [
        types.InlineKeyboardButton(text='сегодня', callback_data='today'),
        types.InlineKeyboardButton(text='завтра', callback_data='tomorrow'),
        types.InlineKeyboardButton(text='понедельник', callback_data='0'),
        types.InlineKeyboardButton(text='вторник', callback_data='1'),
        types.InlineKeyboardButton(text='среда', callback_data='2'),
        types.InlineKeyboardButton(text='четверг', callback_data='3'),
        types.InlineKeyboardButton(text='пятница', callback_data='4'),
        types.InlineKeyboardButton(text='суббота', callback_data='5'),
        types.InlineKeyboardButton(text='вчера', callback_data='yesterday'),
]
