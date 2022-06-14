import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)

menu = types.ReplyKeyboardMarkup(resize_keyboard = True)

btnUSD = types.KeyboardButton(text="🇺🇸 Доллар США")
btnEUR = types.KeyboardButton(text="🇪🇺 Евро")
btnCZK = types.KeyboardButton(text="🇨🇿 Чешская Крона")
btnTRY = types.KeyboardButton(text="🇹🇷 Турецкая Лира")
btnPLN = types.KeyboardButton(text="🇵🇱 Польский Золотой")
btnCHF = types.KeyboardButton(text="🇨🇭 Швейцарский Франк")
btnKZT = types.KeyboardButton(text="🇰🇿 Казахстанский Тенге")
btnJPY = types.KeyboardButton(text="🇯🇵 Японская Йена")
menu.add(btnUSD)
menu.add(btnEUR)
menu.add(btnCZK)
menu.add(btnTRY)
menu.add(btnPLN)
menu.add(btnCHF)
menu.add(btnKZT)
menu.add(btnJPY)



@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Выбери валюту',reply_markup=menu)


@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇪🇺 Евро")
def eur(message):
	text = "1 Евро = "+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇨🇿 Чешская Крона")
def czk(message):
	text = '1 Чешская Крона '+ str(rates['CZK'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇹🇷 Турецкая Лира")
def usd(message):
	text = '1 Турецкая Лира '+ str(rates['TRY'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇵🇱 Польский Золотой")
def pln(message):
	text = '1 Польский Золотой '+ str(rates['PLN'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇨🇭 Швейцарский Франк")
def chf(message):
	text = '1 Швейцарский франк '+ str(rates['CHF'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇰🇿 Казахстанский Тенге")
def kzt(message):
	text = '1 Казахстанский Тенге '+ str(rates['KZT'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text=="🇯🇵 Японская Йена")
def jpy(message):
	text = '1 Японская Йена'+ str(rates['JPY'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)






if __name__ == '__main__':
	bot.infinity_polling()