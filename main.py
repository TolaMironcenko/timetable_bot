import telebot
from telebot import types
import json
from buttons import buttons
from days import get_format_week
from raspToDay import rasptoeveryday
import getrasp
import threading


def main():
    threading.Thread(target=getrasp.get_timetable_json).start()
    print('bot started')

    TOKEN = 'TOKEN'  # raspbot

    bot = telebot.TeleBot(TOKEN)

    with open('rasp.json') as json_file:
        raspdata = json.load(json_file)

    markup = types.InlineKeyboardMarkup()
    markup.row(buttons[2], buttons[3], buttons[4])
    markup.row(buttons[5], buttons[6], buttons[7])
    markup.row(buttons[8], buttons[0], buttons[1])

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        print(call.data)
        raspmessage = 'Расписание на: ' + \
                      get_format_week(int(call.data) if call.data.isdigit() else call.data) + '\n\n' + \
                      rasptoeveryday(get_format_week(int(call.data) if call.data.isdigit() else call.data), raspdata)
        bot.send_message(call.message.chat.id, raspmessage, reply_markup=markup)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        finalMessage = 'Привет это бот расписания ТУСУР факультета систем управления группы 430-3\n\n' \
                       'Расписание на сегодня: ' + get_format_week('today') + '\n\n'

        finalMessage += rasptoeveryday(get_format_week('today'), raspdata)

        bot.send_message(message.chat.id, finalMessage, reply_markup=markup)

    bot.infinity_polling()


if __name__ == "__main__":
    main()
