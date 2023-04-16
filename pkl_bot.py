import telebot
from telebot import types
import requests
import sqlite3
import time
import csv

print('in progress...')
token = '6007672689:AAFQGE3j-NfUkmpLN5zOvflMyuNqRLsnCEc'
bot = telebot.TeleBot(token)
buttons = 1

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    user = message.from_user.id
    print(user)
    if (user == 6011769112) or (user == 5965051017):

        markup = types.ReplyKeyboardMarkup(row_width=1)

        item1 = types.KeyboardButton("Сделать рассылку")
        item2 = types.KeyboardButton("Изменить количество кнопок")

        markup.add(item1, item2)

        bot.send_message(message.chat.id,
                         'Здравствуй,' + str(message.from_user.first_name) + '!\nЧем обязан?'.format(message.from_user,
                                                                                                     bot.get_me()),
                         parse_mode='html', reply_markup=markup)
        if message.text == "Сделать рассылку":
            bot.send_message(message.chat.id,
                             'Отправьте мне сообщение для рассылки')



    else:
        bot.send_message(message.chat.id,
                         'Ты не похож на хозяина. Отправьте команду /start, чтобы воспользоваться ботом')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Автодороги", callback_data='ROAD')
    item2 = types.InlineKeyboardButton("ПГС", callback_data='PGS')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, text=str(
        message.from_user.first_name) + ", Вас приветствует " + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГрупп</a>" + "! Выберите подходящее Вам направление:".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    item1 = types.InlineKeyboardButton("Начать пользоваться ботом", callback_data='START')

    markup.add(item1)

    bot.send_message(message.chat.id,
                     text="Вас приветствует " + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГрупп</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def answer(message):
    user = message.from_user.id
    if (user == 6011769112) or (user == 5965051017):
        if message.text == "Изменить количество кнопок":
            global buttons

            markup = types.ReplyKeyboardMarkup(row_width=1)

            item1 = types.KeyboardButton("[ИИ], [СИД], [Сметы], [ООС]")
            item2 = types.KeyboardButton("[ИИ], [СИД], [Сметы]")
            item3 = types.KeyboardButton("[ИИ], [СИД]")
            item4 = types.KeyboardButton("[ИИ]")

            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "выберите нужное количество содержание меню п.2", reply_markup=markup)

        if message.text == ("[ИИ], [СИД], [Сметы], [ООС]"):

            buttons = 1
            print(buttons)
        elif message.text == ("[ИИ], [СИД], [Сметы]"):

            buttons = 2
            print(buttons)
        elif message.text == ("[ИИ], [СИД]"):
            buttons = 3
            print(buttons)
        elif message.text == ("[ИИ]"):
            buttons = 4
            print(buttons)
        else:
            bot.send_message(message.chat.id, "Готово!")


employee_data = []


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global employee_data
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width=2)
            if call.data == 'ROAD':

                if buttons == 1:

                    markup = types.InlineKeyboardMarkup(row_width=2)

                    item1 = types.InlineKeyboardButton("ИИ", callback_data='3')
                    item2 = types.InlineKeyboardButton("СИД", callback_data='4')
                    item3 = types.InlineKeyboardButton("Сметы", callback_data='5')
                    item4 = types.InlineKeyboardButton("ООС", callback_data='6')
                    item5 = types.InlineKeyboardButton("Назад", callback_data='START')
                    markup.add(item1, item2, item3, item4, item5)

                elif buttons == 2:

                    markup = types.InlineKeyboardMarkup(row_width=2)

                    item1 = types.InlineKeyboardButton("ИИ", callback_data='3')
                    item2 = types.InlineKeyboardButton("СИД", callback_data='4')
                    item3 = types.InlineKeyboardButton("Сметы", callback_data='5')
                    item5 = types.InlineKeyboardButton("Назад", callback_data='START')
                    markup.add(item1, item2, item3, item5)


                elif buttons == 3:
                    markup = types.InlineKeyboardMarkup(row_width=2)

                    item1 = types.InlineKeyboardButton("ИИ", callback_data='3')
                    item2 = types.InlineKeyboardButton("СИД", callback_data='4')
                    item5 = types.InlineKeyboardButton("Назад", callback_data='START')
                    markup.add(item1, item2, item5)

                elif buttons == 3:
                    markup = types.InlineKeyboardMarkup(row_width=2)

                    item1 = types.InlineKeyboardButton("ИИ", callback_data='3')
                    item5 = types.InlineKeyboardButton("Назад", callback_data='START')
                    markup.add(item1, item5)

                msg = "Автодороги, Меню, п.2"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'PGS':

                item1 = types.InlineKeyboardButton("Назад", callback_data='START')
                markup.add(item1)

                msg = "ПГС, Меню, п.2"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == '3':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)
                employee_data = ["ИИ"]
                msg = "ИИ (инженерные изыскания)\nОписание проекта...\n\n\t-Экология\n\t-Геодезия\n\t-Геология\n\t-Прочее"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == '4':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "СИД"
                employee_data = ["СИД"]

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == '5':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "Сметы"
                employee_data = ["Сметы"]

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == '6':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "ООС"
                employee_data = ["ООС"]

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == '7':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("✅ Я подтверждаю своё согласие на обработку персональных данных",
                                                   callback_data='FIO')
                item2 = types.InlineKeyboardButton("Назад", callback_data='3')
                markup.add(item1, item2)

                msg = """*ссылка на ТЗ*\nЕсли Вас заинтересовало объявление, можно на него откликнуться, подвердив согласие на обработку персональных данных по кнопке ниже:"""

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'FIO':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Готово", callback_data='PHONE')
                item2 = types.InlineKeyboardButton("Назад", callback_data='7')
                markup.add(item1, item2)

                msg = "Приступим к заполнению анкеты:\nВведите ФИО"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'PHONE':
                employee_data.append(call.message.text)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Готово", callback_data='TRUE')
                # item2 = types.InlineKeyboardButton("Назад", callback_data='7')
                markup.add(item1)  # , item2)

                msg = "Введите номер телефона:"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'TRUE':
                employee_data.append(call.message.text)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Всё верно!", callback_data='HR')
                item2 = types.InlineKeyboardButton("Ввести данные заново", callback_data='7')
                markup.add(item1, item2)

                msg = "Проверьте, правильно ли введены данные:\t" + str(employee_data)

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'HR':

                item1 = types.InlineKeyboardButton("Вернуться в начало", callback_data='START')
                markup.add(item1)
                msg = "Отлично! Ваши данные записаны. С Вами свяжутся в течение 24 часов."

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            elif call.data == 'START':

                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Автодороги", callback_data='ROAD')
                item2 = types.InlineKeyboardButton("ПГС", callback_data='PGS')

                markup.add(item1, item2)

                msg = "Вас приветствует " + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГрупп</a>" + "! Выберите подходящее Вам направление:"

                bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=markup)

            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
            print(employee_data)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
