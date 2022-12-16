import telebot

bot = telebot.TeleBot('5380562272:AAFqodiUpENCtx7oD8f5xnbIDNOoxJW6YMY')

markup1 = telebot.types.InlineKeyboardMarkup(row_width=1)
markup1_item1 = telebot.types.InlineKeyboardButton('Белый', callback_data='white')
markup1.add(markup1_item1)

markup2 = telebot.types.InlineKeyboardMarkup(row_width=1)
markup2_item1 = telebot.types.InlineKeyboardButton('Черный', callback_data='black')
markup2.add(markup2_item1)


@bot.message_handler(content_types=["text"])
def default_test(message):
    bot.send_message(message.chat.id, text="Нажми", reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'white':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Нажми",
                                  reply_markup=markup2)
        elif call.data == 'black':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Нажми",
                                  reply_markup=markup1)


bot.polling(none_stop=True)


#scheduler = BackgroundScheduler()
#scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=11)
#scheduler.start()