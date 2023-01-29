import telebot
from utils import get_user_profile
from database import insert_user,insert_question,get_question_ids,get_chat_ids
# bot = telebot.TeleBot('5851502480:AAGUUhaTf0kMGvVT0xeCGweJJY36tUFxtUA')
bot = telebot.TeleBot('1643625140:AAHpkVELtF5zgCT9m6_Hc2ZaTvSANesKj64')

import time


leetTracker = False
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    global leetTracker
    bot.reply_to(message, "Howdy, Which Profile you want to track \nType username of the profile?")
    if leetTracker is False:
        print("Called Once")
        leetTracker = True
        inform_user_handler(message)




@bot.message_handler(commands=['get'])
def sign_handler(message):
    global leetTracker
    if leetTracker is False:
        print("Called Again")
        leetTracker = True
        inform_user_handler(message)



@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Tracking is enabled with username: %s" % message.text)
    data = get_user_profile(message.text)
    insert_handler(message,data)

def insert_handler(message, data):
    response =''
    if 'errors' in data:
        horoscope_message = f'*Error:* {data["errors"][0]["message"]}'
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
    else:
        horoscope_message = f'*New Question :\n*{data["data"]["recentAcSubmissionList"][0]["title"]}'
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
        insert_user(message.chat.id,message.text)
        insert_question(data["data"]["recentAcSubmissionList"][0]["id"],message.text)


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
    chat_ids =  get_chat_ids()
    while True:
        user_questions = [] 
        for chatid in chat_ids:
            res = get_question_ids(chatid)
            if res is not None:
                username = res["username"]
                title =res["data"]["data"]["recentAcSubmissionList"][0]["title"]
                difficulty = res["question"]["difficulty"]
                horoscope_message=''
                if difficulty == 'Easy':
                    horoscope_message = "_New Question_ \nUsername: *"+str(username)+"* \nQuestion: *"+str(title)+ "\nDifficulty :"+str(difficulty)+"🟢*"
                if difficulty == 'Medium':
                    horoscope_message = "_New Question_ \nUsername: *"+str(username)+"* \nQuestion: *"+str(title)+ "\nDifficulty :"+str(difficulty)+"🟡*"
                if difficulty == 'Hard':
                    horoscope_message = "_New Question_ \nUsername: *"+str(username)+"* \nQuestion: *"+str(title)+ "\nDifficulty :"+str(difficulty)+"🔴*"
                bot.send_message(chatid, horoscope_message, parse_mode="Markdown")
                obj = {
                    'questionid': res["data"]["data"]["recentAcSubmissionList"][0]["id"],
                    'username': res["username"]
                }
                user_questions.append(obj)
            time.sleep(6)
        for user_question in user_questions:
            insert_question(user_question['questionid'],user_question["username"])
    time.sleep(180)







bot.infinity_polling(timeout=10, long_polling_timeout = 5)
