#!/usr/bin/python
import telebot
import datetime
import time

TOKEN = '1203398903:AAH8GA4fF4xmaNVR82-sTJ1otvAzyvxxyIk'

date = ["06.13", "12.13", "17.13", "01.13"]
chat_id = -1001341971473
user_id = 445671495
n = 9

bot = telebot.TeleBot(TOKEN)

def check_error(n):
    global bot, user_id
    try:
        while True:
            event = bot.get_updates()[n]
            if event.message == None:
                n += 1
            else:
                if event.message.content_type == 'video' and event.message.chat.id == user_id:
                    return n
                else:
                    n += 1
    except IndexError:
        return False

while True:
    for i in date:
        while True:
            now_date = datetime.datetime.today().strftime("%H.%M")
            if now_date == i:
                key = check_error(n)
                if key != False:
                    n = key
                    event = bot.get_updates()[n]
                    date = event.message.video.file_id
                    bot.send_video(chat_id=chat_id, data=date)
                    bot.send_message(chat_id=user_id, text=n)
                    n += 1
                    time.sleep(1000)
                    break
                else:
                    time.sleep(1000)
                    break
