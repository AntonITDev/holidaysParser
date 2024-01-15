from telebot import *
from Parser import Parser_holidays

def main():
	token = ''

	bot = TeleBot(token)
	parser = Parser_holidays()


	@bot.message_handler(commands=['start'])
	def start(msg: types.Message):
		bot.send_message(msg.from_user.id, 'Напишите команду /holidays, чтобы получить все текущие праздники.')


	@bot.message_handler(commands=['holidays'])
	def pars_holiday_hander(msg: types.Message):
		holidays = parser.get_holidays()
		bot.send_message(msg.from_user.id, 'Текущий список праздников:\n'+'\n'.join(holidays))


	bot.infinity_polling()

if __name__ == '__main__':
	main()
