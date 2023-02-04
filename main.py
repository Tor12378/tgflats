import telebot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot import types
bot = telebot.TeleBot('6189070272:AAGodOjSPW6u-Vg_rcvktvJmq3hsshzxRb8')


@bot.message_handler(commands=['help', 'start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Квартиры")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.message_handler(content_types='text')
def welcome(message):
    if message.text == "Квартиры":
        text="Kot"
        with open('img.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text)
    if message.text == "К":
        def start(m):
        calendar, step = DetailedTelegramCalendar().build()


bot.infinity_polling()