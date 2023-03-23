import telebot

# Api Dari Bot Kita
api = "6083747081:AAFYmB9YrzfrGv3QNuxTi_9f9vTJdhLf4Ig"

# pesan 
bot = telebot.TeleBot(api)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Say anything here') 

# apakah bot berjalan
print("Bots are running ...") 
bot.polling()