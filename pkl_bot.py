import telebot
from telebot import types
import requests
import sqlite3
import time

print('in progress...')
token = '6007672689:AAFQGE3j-NfUkmpLN5zOvflMyuNqRLsnCEc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    user = message.from_user.id
    print(user)
    if (user == 6011769112 ):

        markup = types.InlineKeyboardMarkup(row_width=1)

        item1 = types.InlineKeyboardButton("Сделать рассылку", callback_data='MESSAGE')
        item2 = types.InlineKeyboardButton("Посмотреть статистику", callback_data='Stat')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Не верю своим глазам! Ты ли это, {0.first_name}?\nЧем займемся?'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Ты не похож на хозяина')






@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Автодороги", callback_data='ROAD')
    item2 = types.InlineKeyboardButton("ПГС", callback_data='PGS')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, text="{0.first_name}, Вас приветствует ".format(message.from_user, bot.get_me()) + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГруп</a>" +
                                           "! Выберите подходящее Вам направление:".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(call):
    if call.data == "MESSAGE":
        ask = call.message.text
        bot.send_message(call.message.chat.id, ask)

    else:
        msg1 = bot.send_message(call.message.chat.id, 'Пока что я не умею отвечать на сообщения.')
        time.sleep(10)
        bot.delete_message(chat_id=call.message.chat.id, message_id=msg1.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width=2)
            if call.data == 'ROAD':

                item1 = types.InlineKeyboardButton("ИИ", callback_data='3')
                item2 = types.InlineKeyboardButton("СИД", callback_data='4')
                item3 = types.InlineKeyboardButton("Сметы", callback_data='5')
                item4 = types.InlineKeyboardButton("ООС", callback_data='6')
                markup.add(item1, item2, item3, item4)

                msg = "Автодороги, Меню, п.2"

            elif call.data == 'PGS':

                item1 = types.InlineKeyboardButton("Назад", callback_data='ROAD')
                markup.add(item1)

                msg = "ПГС, Меню, п.2"

            elif call.data == '3':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "ИИ (инженерные изыскания)\nОписание проекта...\n\n\t-Экология\n\t-Геодезия\n\t-Геология\n\t-Прочее"

            elif call.data == '4':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "СИД"

            elif call.data == '5':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "Сметы"

            elif call.data == '6':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data='7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')

                markup.add(item1, item2)

                msg = "ООС"


            elif call.data == '7':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("✅ Я подтверждаю своё согласие на обработку персональных данных",
                                                   callback_data='FIO')
                item2 = types.InlineKeyboardButton("Назад", callback_data='3')
                markup.add(item1, item2)

                msg = """*ссылка на ТЗ*\nЕсли Вас заинтересовало объявление, можно на него откликнуться, подвердив согласие на обработку персональных данных по кнопке ниже:"""

            elif call.data == 'FIO':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Готово", callback_data='PHONE')
                item2 = types.InlineKeyboardButton("Назад", callback_data='7')
                markup.add(item1, item2)

                msg = "Приступим к заполнению анкеты:\nВведите ФИО"

            elif call.data == 'PHONE':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Готово", callback_data='TRUE')
                item2 = types.InlineKeyboardButton("Назад", callback_data='7')
                markup.add(item1, item2)

                msg = "Введите номер телефона:"

            elif call.data == 'TRUE':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Всё верно!", callback_data='HR')
                item2 = types.InlineKeyboardButton("Ввести данные заново", callback_data='7')
                markup.add(item1, item2)

                msg = "Проверьте, правильно ли введены данные"

            elif call.data == 'HR':

                item1 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data='ROAD')
                markup.add(item1)

                msg = "Отлично! Ваши данные записаны. С Вами свяжутся в течение 24 часов."

            elif call.data == 'MESSAGE':

                msg = ("Отправьте мне сообщение для рассылки")

                #ask = call.message.text
                #bot.send_message(call.message.chat.id, ask)

            bot.send_message(call.message.chat.id, text=msg.format(call.message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)