import telebot
import sqlite3
import Tsort
import adminComands
import check
import startCheck
import checkUserType
import getOrders
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
feedbackMode = False

newUser = True
userType = False

selectionTshirt = ''
selectionSize = ' '
selectionAdress = ''
selectionPhone = ''
selectionName = ''
selectionDelivery = ' '
feedback = ' sdf'

hideBoard = types.ReplyKeyboardRemove()

adminComands.getOrders()

@bot.message_handler(content_types=['location'])
def location(message):
    print(message)

    global selectionAdressMode
    global selectionDeliveryMode
    global selectionAdress

    if selectionAdressMode:
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)

        keyboard.row("Почта России", "СДЭК")
        bot.send_message(message.chat.id, "Теперь давай выберем способ доставки", reply_markup=keyboard)
        selectionAdress = str(message.location.longitude) + " " + str(message.location.latitude)
        selectionDeliveryMode = True
        selectionAdressMode = False


@bot.message_handler(content_types=['contact'])
def contact(message):
    print(message)

    global selectionPhoneMode
    global selectionNameMode
    global selectionPhone

    if selectionPhoneMode:
        bot.send_message(message.chat.id, "Как к Вам обращаться?", reply_markup=hideBoard)
        # bot.send_message(message.chat.id, message)
        selectionPhone = message.contact.phone_number
        selectionNameMode = True
        selectionPhoneMode = False
        check.check_phone(message.contact.phone_number)
        print(check.check_phone(message.contact.phone_number))

@bot.message_handler(commands=["order"])
def getOrders(message):
    #adminComands.getOrders(message.from_user.id)
    print("123")

@bot.message_handler(commands=['start'])
def start_message(message):

    global userType

    startCheck.start(message)

    if checkUserType.checkUserType(message.from_user.id):
        bot.send_message(message.chat.id, "Я вас узнал вы админ, для вас доступны функции \n"
                                          "/add - обавление \n"
                                          "/edit - изменение\n"
                                          "/test")
        userType = True

    bot.send_message(message.chat.id, "/catalog - каталог футболок \n"
                                      "/help - помощь\n")


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


@bot.message_handler(commands=["test"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправьте  свой номер телефона или поделись местоположением", reply_markup=keyboard)

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
    global feedbackMode

    global selectionTshirt
    global selectionSize
    global selectionAdress
    global selectionPhone
    global selectionName
    global selectionDelivery

    if feedbackMode:
        feedback = Text
        selection = (selectionTshirt + "\nразмер" + selectionSize + "\nадрес:" + str(selectionAdress) + "\nВаш номер:" + str(selectionPhone)
                     + "\nспособ связи "+ feedback)

        getOrders.order(message.from_user.id,selectionTshirt, selectionSize, selectionAdress, selectionPhone, selectionName, selectionDelivery,feedback)
        bot.send_message(message.chat.id,selection , reply_markup = hideBoard )
        feedbackMode = False



    if selectionNameMode:
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)

        keyboard.row("Телефон", "telegram","whatsapp", "viber")
        bot.send_message(message.chat.id, "Где с вами лучше связаться для подтверждения заказа", reply_markup = keyboard )
        #selection = (selectionTshirt + "\nразмер" + selectionSize + "\nадрес:" + str(selectionAdress) + "\nВаш номер:" + str(selectionPhone))



        selectionName = Text
        feedbackMode = True
        selectionNameMode = False


    if selectionPhoneMode:
        if check.check_phone(Text):
            bot.send_message(message.chat.id, "Как к вам обращаться?", reply_markup=hideBoard)
            selectionPhone = Text
            selectionNameMode = True
            selectionPhoneMode = False
        else:
            bot.send_message(message.chat.id, "кажется вы неправильно ввели номер", reply_markup=hideBoard)

    if selectionDeliveryMode:

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id, "Cкажите Ваш номер", reply_markup=keyboard)


        #bot.send_message(message.chat.id, "Cкажите Ваш номер", reply_markup=hideBoard)
        selectionDelivery = Text
        selectionPhoneMode = True
        selectionDeliveryMode = False

    if selectionAdressMode:
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)

        keyboard.row("Почта России", "СДЭК")
        bot.send_message(message.chat.id, "Теперь давай выберем способ доставки", reply_markup=keyboard)
        selectionAdress = Text
        selectionDeliveryMode = True
        selectionAdressMode = False

    if selectionSizeMode:
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)

        button_geo = types.KeyboardButton(text="Отправить   местоположение", request_location=True)
        keyboard.add(button_geo)

        bot.send_message(message.chat.id, "Хорошо, теперь скажите куда вам доставить", reply_markup=keyboard)
        bot.send_message(message.chat.id, "P.S. инода надо подождать пока всёпуе загрузиться")

        selectionSize = Text
        selectionAdressMode = True
        selectionSizeMode = False

    if selectionTshirtMode:
        Tsort.showTSort(message.chat.id, Text)
        selectionTshirt = Text

        selectionTshirtMode = False
        selectionSizeMode = True




if __name__ == "__main__":
    bot.polling()
