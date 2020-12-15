import telebot

TOKEN = '1444766312:AAHV4m7J5tFQ0fRVE6ot4wlUrlRsR2JQxek'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling()
#print(bot.getMe())

# def handle(msg):
#     """ Process request like '3+2' """
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     text = msg["text"]
#     try:
#         answer = eval(text)
#     except:
#         answer = "Can't calculate :("
#     bot.sendMessage(chat_id, "answer: {}".format(answer))
#
#
# MessageLoop(bot, handle).run_as_thread()
#
# # Keep the program running.
# while True:
#     n = input('To stop enter "stop":')
#     if n.strip() == 'stop':
#         break