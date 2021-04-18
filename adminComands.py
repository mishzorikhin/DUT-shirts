import telebot
import sqlite3

conn = sqlite3.connect('DUTShirts.db')
cur = conn.cursor()

conn.commit()
bot = telebot.TeleBot("1765121821:AAEsuZbDzF9W215pKIAmE_VDBxcSu_lpa5Y")



