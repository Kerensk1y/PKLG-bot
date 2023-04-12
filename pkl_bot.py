import telebot
from telebot import types
import config
import requests
import aiogram
import sqlite3
import time

print('in progress...')
token = '6007672689:AAFQGE3j-NfUkmpLN5zOvflMyuNqRLsnCEc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.InlineKeyboardMarkup(row_width = 2)
    
    item1 = types.InlineKeyboardButton("Автодороги", callback_data = '1')
    item2 = types.InlineKeyboardButton("ПГС", callback_data = '2')
    
    markup.add(item1, item2)

    bot.send_message(message.chat.id, text = "{0.first_name}, Вас приветствует ".format(message.from_user, bot.get_me()) + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГруп</a>" + "! Выберите подходящее Вам направление:".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if True:
        msg1 = bot.send_message(message.chat.id, 'Пока что я не умею отвечать на сообщения.')
        bot.delete_message(chat_id = message.chat.id, message_id = msg1.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width = 2)
            if call.data == '1':
                
                item1 = types.InlineKeyboardButton("ИИ", callback_data = '3')
                item2 = types.InlineKeyboardButton("СИД", callback_data = '4')
                item3 = types.InlineKeyboardButton("Сметы", callback_data = '5')
                item4 = types.InlineKeyboardButton("ООС", callback_data = '6')
                markup.add(item1, item2, item3, item4)
                
                msg = "Автодороги, Меню, п.2"
                                     
            elif call.data == '2':
                
                item1 = types.InlineKeyboardButton("Назад", callback_data = '1')
                markup.add(item1)
                
                msg = "ПГС, Меню, п.2"
                            
            elif call.data == '3':

                item1 = types.InlineKeyboardButton("Запросить ТЗ и дополнительную информацию", callback_data = '7')
                item2 = types.InlineKeyboardButton("Вернуться в меню, п.2", callback_data = '1')
                
                markup.add(item1, item2)
                
                msg = "ИИ (инженерные изыскания)\nОписание проекта...\n\n\t-Экология\n\t-Геодезия\n\t-Геология\n\t-Прочее"                

            elif call.data == '4':
            
                item1 = types.InlineKeyboardButton("Назад", callback_data = '1')
                markup.add(item1)
            
                msg = "СИД"
            
            elif call.data == '5':
            
                item1 = types.InlineKeyboardButton("Назад", callback_data = '1')
                markup.add(item1)
                
                msg = "Сметы"
                
            elif call.data == '6':
                
                item1 = types.InlineKeyboardButton("Назад", callback_data = '1')
                markup.add(item1)
            
                msg = "ООС"

            elif call.data == '7':
                
                item1 = types.InlineKeyboardButton("Назад", callback_data = '3')
                markup.add(item1)
                
                msg = "*здесь могла быть ваша ссылка на гугл или яндекс форму*"

            bot.send_message(call.message.chat.id, text = msg.format(call.message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)    
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id = call.message.message_id)
                 
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
