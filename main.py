import telebot
import sqlite3
import Tsort
from telebot import types


bot = telebot.TeleBot("1765121821:AAEsuZbDzF9W215pKIAmE_VDBxcSu_lpa5Y")

conn = sqlite3.connect('DUTShirts.db')
cur = conn.cursor()


selectionTshirtMode = False
selectionSizeMode = False
selectionAdressMode = False
selectionPhoneMode = False
selectionNameMode = False
selectionDeliveryMode = False


selectionTshirt = ''
selectionSize = ' '
selectionAdress = ''
selectionPhone = ''
selectionName = ''
selectionDelivery = ' '

hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "/TShirts - каталог футболок \n"
                                      #"/orders - заказы"
                                      "/help - помощь")
    print(message)

@bot.message_handler(commands=['TShirts'])
def start_message(message):

    Tsort.showTSorts(message.chat.id)
    global selectionTshirtMode
    selectionTshirtMode = True
    print(message)




@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Здесь будет помощь")
    print(message)

@bot.message_handler(content_types=['text'])
def text_message(message):
    Text = message.text
    print(message)
    global selectionTshirtMode
    global selectionSizeMode
    global selectionAdressMode
    global selectionPhoneMode
    global selectionNameMode
    global selectionDeliveryMode

    global selectionTshirt
    global selectionSize
    global selectionAdress
    global selectionPhone
    global selectionName
    global selectionDelivery

    if (selectionNameMode):
        bot.send_message(message.chat.id,"Ok")
        check=  (selectionTshirt + "\nразмер"+ selectionSize + "\nадрес:"+ selectionAdress+ "\nВаш номер:"+ selectionPhone)
        bot.send_message(message.chat.id, check)
        selectionName = Text
        selectionNameMode = False

    if (selectionPhoneMode):
        bot.send_message(message.chat.id,"Как к вам обращаться?")
        selectionPhone = Text
        selectionNameMode = True
        selectionPhoneMode = False


    if (selectionDeliveryMode):
        bot.send_message(message.chat.id,"Cкажите вам номер", reply_markup=hideBoard)
        selectionDelivery = Text
        selectionPhoneMode = True
        selectionDeliveryMode = False


    if (selectionAdressMode):
        hints = telebot.types.ReplyKeyboardMarkup(True, False)

        hints.row("почта России", "СДЭК")
        bot.send_message(message.chat.id,"Теперь давай выберем способ доставки",reply_markup=hints)
        selectionAdress = Text
        selectionDeliveryMode = True
        selectionAdressMode = False

    if (selectionSizeMode):
        bot.send_message(message.chat.id,"Хорошо, теперь скажите куда вам доставить", reply_markup=hideBoard)
        selectionSize = Text
        selectionAdressMode = True
        selectionSizeMode = False

    if (selectionTshirtMode):
        Tsort.showTSort(message.chat.id, Text)
        selectionTshirt = Text

        selectionTshirtMode = False
        selectionSizeMode = True


@bot.message_handler(content_types=['photo'])
def set_photo(message):
    print(message)


if __name__ == "__main__":
    bot.polling()
