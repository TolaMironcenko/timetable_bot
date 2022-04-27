import json
from days import get_format_week
from raspToDay import rasp_to_every_day, get_pare
import getrasp
import threading
import datetime
import time
from bot import bot
from bot.bot import get_file
from get_chat_id import get_chat_id
from termcolor import cprint


def get_chats_ids():
    with open('users.json', 'r') as get_chat_ids:
        chat_ids = json.load(get_chat_ids)
        return chat_ids


print('bot started')


def notifications():
    while True:
        pare = ''
        for i in get_file():
            if i['date'].find(get_format_week('today')) != -1:
                start = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d') + ' ' +
                                                   i['time']['start'], '%Y-%m-%d %H:%M')
                now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M') + ':00',
                                                 '%Y-%m-%d %H:%M:%S')
                delt20 = now + datetime.timedelta(minutes=20)
                delt = start == delt20
                if delt:
                    pare = 'Через 20 минут начнется пара:\n\n' + get_pare(get_format_week('today'), pare, i)
                    with open('users.json') as users:
                        users_data = json.load(users)
                    for j in users_data:
                        bot.bot.send_message(j['chat_id'], pare)
                    pare = ''
                    cprint('ok', 'green')
        cprint('no', 'blue')
        time.sleep(60)


def main():

    @bot.bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        print(call.data)
        raspmessage = 'Расписание на: ' + \
                      get_format_week(int(call.data) if call.data.isdigit() else call.data) + '\n\n' + \
                      rasp_to_every_day(get_format_week(int(call.data) if call.data.isdigit() else call.data),
                                        get_file())
        bot.bot.send_message(call.message.chat.id, raspmessage, reply_markup=bot.markup)

    @bot.bot.message_handler(commands=['start', 'date'])
    def send_welcome(message):
        if message.text.split(' ')[0] == '/start':
            final_message = 'Привет это бот расписания ТУСУР факультета систем управления группы 430-3\n\n' \
                            'Расписание на сегодня: ' + get_format_week('today') + '\n\n'

            final_message += rasp_to_every_day(get_format_week('today'), get_file())

            bot.bot.send_message(message.chat.id, final_message, reply_markup=bot.markup)

        if message.text.split(' ')[0] == '/date':
            final_message = 'Расписание на: ' + message.text.split(' ')[1] + '\n\n'
            final_message += rasp_to_every_day(message.text.split(' ')[1], get_file())
            bot.bot.send_message(message.chat.id, final_message, reply_markup=bot.markup)

        get_chat_id.get_id(message, get_chats_ids())

    while True:
        try:
            threading.Thread(target=getrasp.get_timetable_json).start()
            threading.Thread(target=notifications).start()
            bot.bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            cprint(str(e), 'red')


if __name__ == "__main__":
    Process(target=main()).start()
