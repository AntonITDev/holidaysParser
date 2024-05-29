from telebot import *
from telebot.types import Message
from Parser import Parser_holidays
import config

bot = TeleBot(config.token)
parser = Parser_holidays()


@bot.message_handler(commands=['start'])
def start_handler(message: Message):
	bot.send_message(message.from_user.id, 'Напишите команду /holidays, чтобы получить все текущие праздники.')


@bot.message_handler(commands=['holidays'])
def pars_holiday_hander(message: Message):
	holidays = parser.get_holidays()
	bot.send_message(message.from_user.id, 'Текущий список праздников:\n'+'\n'.join(holidays))


def run():
	bot.infinity_polling()