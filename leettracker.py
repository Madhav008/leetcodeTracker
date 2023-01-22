import telebot
from utils import get_user_profile
from database import insert_user,insert_question,get_question_ids
bot = telebot.TeleBot('5851502480:AAGUUhaTf0kMGvVT0xeCGweJJY36tUFxtUA')
import time

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, Which Profile you want to track \nType username of the profile?")



@bot.message_handler(commands=['get'])
def sign_handler(message):
    res = get_question_ids(message.chat.id)
    if res is not None:
        while True:
            res = get_question_ids(message.chat.id)
            if res is not None:
                inform_user_handler(message)
                time.sleep(1)
    else:
        text = "First Set The *Usernames*."
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")



@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Tracking is enabled with username: %s" % message.text)
    data = get_user_profile(message.text)
    profile_handler(message,data)







def profile_handler(message, data):
    response =''
    if 'errors' in data:
        horoscope_message = f'*Error:* {data["errors"][0]["message"]}'
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
    else:
        horoscope_message = f'*New Question :\n*{data["data"]["recentAcSubmissionList"][0]["title"]}'
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
        insert_user(message.chat.id,message.text)
        insert_question(data["data"]["recentAcSubmissionList"][0]["id"],message.text)
        inform_user_handler(message)

def inform_user_handler(message):
    while True:
        chatid = message.chat.id
        res = get_question_ids(chatid)
        if res is not None:
            horoscope_message = f'*New Question\n*{res["username"]}*:\n*{res["data"]["data"]["recentAcSubmissionList"][0]["title"]}'
            bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
            insert_question(res["data"]["data"]["recentAcSubmissionList"][0]["id"],res["username"])
        time.sleep(60)







bot.infinity_polling(timeout=10, long_polling_timeout = 5)
