import telebot
token=''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'aaaaaa')
bot.polling()
