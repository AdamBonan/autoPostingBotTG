import telebot
import sqlite3

TOKEN = '1203398903:AAH8GA4fF4xmaNVR82-sTJ1otvAzyvxxyIk'
bot = telebot.TeleBot(TOKEN)

user_id = 445671495
update_id = 0

def set_db():
	conn = sqlite3.connect("file_id.db")
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE events (update_id int, file_id text)""")
	conn.commit()
	conn.close()

def update_db(update_id, file_id):
	conn = sqlite3.connect("file_id.db")
	cursor = conn.cursor()
	cursor.execute("""INSERT INTO events VALUES ({0}, '{1}')""".format(update_id, file_id))
	conn.commit()
	conn.close()

@bot.message_handler(content_types=['video'])
def get_text_messages(event):
	global update_id, user_id
	if event.from_user.id == user_id:
		file_id = event.video.file_id
		update_db(update_id, file_id)
		update_id += 1

bot.polling(none_stop=True, interval=0)