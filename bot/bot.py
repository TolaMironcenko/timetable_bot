import telebot
from telebot import types
from buttons import buttons
import json

token = 'token'  # testbot

bot = telebot.TeleBot(token)

with open('rasp.json') as json_file:
    raspdata = json.load(json_file)

markup = types.InlineKeyboardMarkup()
markup.row(buttons[2], buttons[3], buttons[4])
markup.row(buttons[5], buttons[6], buttons[7])
markup.row(buttons[8], buttons[0], buttons[1])