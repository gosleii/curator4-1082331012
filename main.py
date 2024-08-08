import telebot
from telebot import types

GET_NAME = False

bot = telebot.TeleBot('1943033886:AAFAvYWNCLzPDTQd6887lCI88z_QGAdthyk')



@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Ну привет, если не шутишь!")


@bot.message_handler(commands=["new"])
def new_handler(message):
    bot.send_message(message.chat.id, "*Давай!*", parse_mode="Markdown")


@bot.message_handler(commands=["look"])
def look_handler(message):
    bot.send_message(message.chat.id, "[Тебе сюда: ](http://button.dekel.ru/)", parse_mode="Markdown")


@bot.message_handler(commands=["send"])
def send_handler(message):
    bot.send_message(message.chat.id, "*Очень умное высказывание*", parse_mode="Markdown")


@bot.message_handler(commands=["get"])
def get_handler(message):
    global GET_NAME
    bot.send_message(message.chat.id,
                     "Сообщите имя бота для проверки. \nПравила именования:\n1. Длина имени не более 20 символов\n2. Имя не начинается с цифры\n3. Имя заканчивается на слово bot",
                     parse_mode="Markdown")
    GET_NAME = True


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global GET_NAME
    if GET_NAME == True:
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        GET_NAME = False

        if (len(message.text) <= 20) and (message.text[0] not in num) and (message.text[-3:] == 'bot'):
            bot.send_message(message.from_user.id, "*Ник одобрен!*", parse_mode="Markdown")
        else:
            v = ''
            if len(message.text) > 20: v = "Слишком длинное имя. "
            if message.text[0] in num: v = v + "\nИмя начинается с цифры. "
            if message.text[-3:] != 'bot': v = v + "\nИмя не заканчивается на слово bot."
            bot.send_message(message.from_user.id, "*" + v + "*", parse_mode="Markdown")

    if message.text.lower() == 'привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Погода')
        btn2 = types.KeyboardButton('Имя бота')
        btn3 = types.KeyboardButton('Советы')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)


    elif message.text.lower() == 'погода':
        bot.send_message(message.from_user.id,
                         'Погоду можно посмотреть тут: ' + '[Gismeteo.ru](https://www.gismeteo.ru/weather-nizhny-tagil-4478/)',
                         parse_mode='Markdown')

    elif message.text.lower() == 'имя бота':
        bot.send_message(message.from_user.id,
                         "Сообщите имя бота для проверки. \nПравила именования:\n1. Длина имени не более 20 символов\n2. Имя не начинается с цифры\n3. Имя заканчивается на слово bot",
                         parse_mode="Markdown")
        GET_NAME = True

    elif message.text.lower() == 'советы':
        bot.send_message(message.from_user.id, 'Советую заглянуть сюда ' + '[ссылка](https://habr.com/)',
                         parse_mode='Markdown')

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Даже и не знаю что сказать...', reply_markup=markup)


bot.infinity_polling()