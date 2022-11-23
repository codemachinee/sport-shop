import telebot

bot = telebot.TeleBot('5380562272:AAFqodiUpENCtx7oD8f5xnbIDNOoxJW6YMY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''Я пробил инфрмацию:

id чата: {message.chat.id}
id пользователя: {message.from_user.id}
имя: {message.from_user.first_name}
фамилия: {message.from_user.last_name}
псевдоним: {message.from_user.username}

текст сообщения: {message.text}''')


bot.polling()