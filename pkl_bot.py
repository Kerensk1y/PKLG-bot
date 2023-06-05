import telebot
from telebot import types
import time
from g_upd import *
from messages import *
from openpyxl import load_workbook

print('in progress...')

zap = False
s = 0
a = ''
token = "6029573477:AAF-NAWPyOXrlTLNQH48y4-4UWVVw4dMUhA"
bot = telebot.TeleBot(token)

admins = [5965051017, 6011769112]

'''
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    user = message.from_user.id
    print(user)
    if user in admins:

        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Изменить количество кнопок", callback_data='QUAN_BUT')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Здравствуй, админ!\nЧем обязан?', reply_markup=markup)

    else:
        bot.send_message(message.chat.id,
                         'Ты не похож на хозяина. Отправьте команду /start, чтобы воспользоваться ботом')
'''

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Проектирование АД", callback_data='ROAD')
    item2 = types.InlineKeyboardButton("Проектирование ПГС", callback_data='PGS')
    markup.add(item1, item2)

    bot.send_photo(message.chat.id, open('headers/start.png', 'rb'), caption=startmsg, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    item1 = types.InlineKeyboardButton("Начать пользоваться ботом", callback_data='START')

    markup.add(item1)

    bot.send_message(message.chat.id,
                     text="Вас приветствует " + "<a href = 'https://www.pk-lidergroup.ru/'>ПК ЛидерГрупп</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


employee_data = [a]
callbkz = ['FIO', 'PHONE', 'MAIL', 'DOP', 'TRUE', 'TZ']


@bot.message_handler(content_types=['text'])
def answer(message):
    global zap, s, callbkz
    if zap:
        markup = types.InlineKeyboardMarkup(row_width=1)
        print(callbkz[s])
        if 0 <= s <= len(callbkz) - 1:
            item1 = types.InlineKeyboardButton("Готово", callback_data=callbkz[s + 1])
            item2 = types.InlineKeyboardButton("Назад", callback_data=callbkz[s - 1])
            markup.add(item1, item2)
            employee_data.append(message.text)
            bot.reply_to(message, 'Записал, нажмите "Готово" для продолжения', reply_markup=markup)
        else:
            s = 0
    else:
        msg1 = bot.send_message(message.chat.id, 'Пока что бот не умеет отвечать на сообщения.')
        time.sleep(10)
        bot.delete_message(chat_id=message.chat.id, message_id=msg1.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global employee_data, zap, a, s
    if call.message:
        markup = types.InlineKeyboardMarkup(row_width=1)
        zapros = 'Запросить техническое задание'
        if call.data == 'ROAD':
            s = 0
            zap = False
            item1 = types.InlineKeyboardButton(ii_but, callback_data='II')
            item2 = types.InlineKeyboardButton(sid_but, callback_data='SID')
            item3 = types.InlineKeyboardButton(smet_but, callback_data='SMET')
            item4 = types.InlineKeyboardButton(oos_but, callback_data='OOS')
            item5 = types.InlineKeyboardButton(isso_but, callback_data='ISSO')
            item6 = types.InlineKeyboardButton(ad_but, callback_data='AD')
            item7 = types.InlineKeyboardButton(proch_but, callback_data='PROCH')
            item8 = types.InlineKeyboardButton(kad_but, callback_data='KAD')
            item9 = types.InlineKeyboardButton("Назад", callback_data='START')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
            msg = menu_admsg
            bot.send_photo(call.message.chat.id, open('headers/menu_ad.png', 'rb'), caption=msg, reply_markup=markup)
            employee_data = []

        elif call.data == 'PGS':
            s = 0
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Назад", callback_data='START')
            markup.add(item1, item2)
            a = 'ПГС'
            msg = pgsmsg
            bot.send_photo(call.message.chat.id, open('headers/pgs.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'II':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = ii_but
            msg = iimsg
            bot.send_photo(call.message.chat.id, open('headers/ii.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'ISSO':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = isso_but
            msg = issomsg
            bot.send_photo(call.message.chat.id, open('headers/isso.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'KAD':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = kad_but
            msg = kadmsg
            bot.send_photo(call.message.chat.id, open('headers/kad.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'SMET':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = smet_but
            msg = smetmsg
            bot.send_photo(call.message.chat.id, open('headers/smet.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'PROCH':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = proch_but
            msg = prochmsg
            bot.send_photo(call.message.chat.id, open('headers/proch.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'SID':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = sid_but
            msg = sidmsg
            bot.send_photo(call.message.chat.id, open('headers/sid.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'OOS':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = oos_but
            msg = oosmsg
            bot.send_photo(call.message.chat.id, open('headers/oos.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'AD':
            zap = False
            item1 = types.InlineKeyboardButton(zapros, callback_data='TZ')
            item2 = types.InlineKeyboardButton("Вернуться в меню", callback_data='ROAD')
            markup.add(item1, item2)
            a = ad_but
            msg = admsg
            bot.send_photo(call.message.chat.id, open('headers/ad.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'TZ':
            s = 5
            zap = False
            item1 = types.InlineKeyboardButton("✅ Получить ТЗ с подтверждением согласия на обработку персональных данных",
                                               callback_data='FIO')
            item2 = types.InlineKeyboardButton("Назад", callback_data='ROAD')
            markup.add(item1, item2)
            msg = tzmsg
            bot.send_photo(call.message.chat.id, open('headers/tz.png', 'rb'), caption=msg, reply_markup=markup)

        elif call.data == 'FIO':
            s = 0
            employee_data = [a]
            zap = True
            msg = "Приступим к заполнению анкеты:\nВведите ФИО"
            bot.send_message(call.message.chat.id, text=msg)

        elif call.data == 'PHONE':
            s = 1
            zap = True
            msg = "Введите номер телефона:"
            bot.send_message(call.message.chat.id, text=msg)

        elif call.data == 'MAIL':
            s = 2
            zap = True
            msg = "Введите почту:"
            bot.send_message(call.message.chat.id, text=msg)

        elif call.data == 'DOP':
            s = 3
            zap = True
            msg = "Введите дополнительную информацию: ссылку на диск с портфолио, опытом работы или резюме."
            bot.send_message(call.message.chat.id, text=msg)

        elif call.data == 'TRUE':
            s = 4
            zap = False
            item1 = types.InlineKeyboardButton("Данные подтверждаю", callback_data='HR')
            item2 = types.InlineKeyboardButton("Исправить данные", callback_data='FIO')
            markup.add(item1, item2)
            out = ''
            for i in range(len(employee_data)):
                if i != len(employee_data) - 1:
                    out += employee_data[i] + ', '
                else:
                    out += employee_data[i]
            msg = "Проверьте, правильно ли введены данные:\t" + str(out)
            bot.send_message(call.message.chat.id, text=msg, reply_markup=markup)

        elif call.data == 'HR':
            zap = False
            item1 = types.InlineKeyboardButton("Вернуться в начало", callback_data='START')
            markup.add(item1)
            msg = hrmsg
            bot.send_photo(call.message.chat.id, open('headers/hr.png', 'rb'), caption=msg, reply_markup=markup)
            # app_table(a, employee_data[1], employee_data[2], employee_data[3], employee_data[4])
            fn = 'test.xlsx'
            wb = load_workbook(fn)
            ws = wb['Заявки']
            ws.append(employee_data)
            wb.save(fn)
            wb.close()
            employee_data = []
            main()

        elif call.data == 'START':

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Проектирование АД", callback_data='ROAD')
            item2 = types.InlineKeyboardButton("Проектирование ПГС", callback_data='PGS')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, open('headers/start.png', 'rb'), caption=startmsg, reply_markup=markup)

        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)


def poll():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        # Retry polling after 3 seconds
        time.sleep(3)
        poll()


if __name__ == '__main__':
    poll()
