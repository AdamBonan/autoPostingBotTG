import telebot
import datetime
import sqlite3

TOKEN = '1203398903:AAH8GA4fF4xmaNVR82-sTJ1otvAzyvxxyIk'
bot = telebot.TeleBot(TOKEN)

date = ["06.07", "12.07", "17.07", "01.07"]
user_id = 445671495
chat_id = -1001341971473
update_id = 0

bot.send_video(chat_id=chat_id, data="BAACAgIAAxkBAAOsXq4OyLhFMITaNVWC9GnFfEDSRBkAAp4FAAK7PWhLcxHtX7Q5Ey0ZBA")
def get_file_id(update_id):
    conn = sqlite3.connect("file_id.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT file_id FROM events WHERE update_id={0}""".format(update_id))
        other = cursor.fetchall()
        cursor.execute("""DELETE FROM events WHERE update_id={0}""".format(update_id))
        conn.commit()
        conn.close()
        return other
    except:
        return False

while True:
    for i in date:
        while True:
            now_date = datetime.datetime.today().strftime("%H.%M")
            if now_date == i:
                key = get_file_id(update_id)[0][0]
                if key != False:
                    file_id = key
                    bot.send_video(chat_id=chat_id, data=file_id)
                    bot.send_message(chat_id=user_id, text=update_id)
                    update_id += 1
                    break
                else:
                    break