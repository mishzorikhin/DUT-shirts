import telebot
import sqlite3
import Tsort
import check
import startCheck
import checkUserType
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

newUser = True
userType = False



selectionTshirt = ''
selectionSize = ' '
selectionAdress = ''
selectionPhone = ''
selectionName = ''
selectionDelivery = ' '

hideBoard = types.ReplyKeyboardRemove()

@bot.message_handler(content_types=['contact'])
def contact(message):
    print(message)

    global selectionPhoneMode
    global selectionNameMode
    global selectionPhone


    if (selectionPhoneMode):
            bot.send_message(message.chat.id, "Как к Вам обращаться?")
            #bot.send_message(message.chat.id, message)
            selectionPhone = message.contact.phone_number
            selectionNameMode = True
            selectionPhoneMode = False
            check.check_phone(message.contact.phone_number)
            print(check.check_phone(message.contact.phone_number))




@bot.message_handler(commands=['start'])
def start_message(message):
    global userType


    startCheck.start(message)

    if(checkUserType.checkUserType(message.from_user.id)):
        bot.send_message(message.chat.id, "Я вас узнал вы админ, для вас доступны функции \n"
                            "/add - обавление \n"
                            "/edit - изменение"
                            )
        userType = True


    bot.send_message(message.chat.id, "/catalog - каталог футболок \n"
                                      #"/orders - заказы"
                                      "/help - помощь")


@bot.message_handler(commands=['catalog'])
def start_message(message):

    Tsort.showTSorts(message.chat.id)
    global selectionTshirtMode
    selectionTshirtMode = True
    print(message.text)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Здесь будет помощь")
    print(message)

@bot.message_handler(content_types=['text'])
def text_message(message):
    Text = message.text
    print(message.text)
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
        selection = (selectionTshirt + "\nразмер"+ selectionSize + "\nадрес:"+ selectionAdress+ "\nВаш номер:"+ selectionPhone)
        print(selection)
        bot.send_message(message.chat.id, selection)
        selectionName = Text
        selectionNameMode = False

    if (selectionPhoneMode):
        if (check.check_phone(Text)):
            bot.send_message(message.chat.id, "Как к вам обращаться?")
            selectionPhone = Text
            selectionNameMode = True
            selectionPhoneMode = False
        else:
            bot.send_message(message.chat.id, "кажется вы неправильно ввели номер")


    if (selectionDeliveryMode):
        bot.send_message(message.chat.id,"Cкажите Ваш номер", reply_markup=hideBoard)
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


if __name__ == "__main__":
    bot.polling()
