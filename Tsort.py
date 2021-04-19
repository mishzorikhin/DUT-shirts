import telebot
import sqlite3
from telebot import types
import main

bot = telebot.TeleBot("1765121821:AAEsuZbDzF9W215pKIAmE_VDBxcSu_lpa5Y")


allName = ""

hideBoard = types.ReplyKeyboardRemove()



def showTSorts(userID):
    # Запрос в базе
    # запись в массив


    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM TShirts;")
    all_result = cur.fetchall()


    for i in range(3):

        sizeS = all_result[i][3]
        sizeM = all_result[i][4]
        sizeL = all_result[i][5]

        stock = ":S, M, L"

        hints = telebot.types.ReplyKeyboardMarkup(True, False)

        hints.row("1","2",'3')

        caption =  (all_result[i][1]  + "\nцена:"+ str(all_result[i][2]) + "\nразмары в наличии" + stock)
        bot.send_photo(userID, all_result[i][6], caption, reply_markup=hints)




def showTSort(userID, TSort):
    conn = sqlite3.connect('DUTShirts.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM TShirts WHERE id = ?;", TSort)
    all_result = cur.fetchall()

    hints = telebot.types.ReplyKeyboardMarkup(True, False)

    hints.row("S", "M", 'L')

    bot.send_message(userID, "Выберете размер" , reply_markup=hints)

