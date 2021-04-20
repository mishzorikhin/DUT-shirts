import telebot
import sqlite3

bot = telebot.TeleBot("1765121821:AAEsuZbDzF9W215pKIAmE_VDBxcSu_lpa5Y")


def getOrders():
    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()
    searchID = "SELECT * FROM orders WHERE status=0"

    cur.execute(searchID)
    results = cur.fetchall()
    for i in results:
        print(i[2])
