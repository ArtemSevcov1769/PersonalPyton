import telebot
from telebot import types
import data_based
bot = telebot.TeleBot('7036308915:AAGwZ3I90LgBG_KfrJiXkhjZWK_JNVxomXY')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton("Математика"), types.KeyboardButton("Русский"))
    markup.add(types.KeyboardButton("Биология"), types.KeyboardButton("География"))
    markup.add(types.KeyboardButton("Физика"), types.KeyboardButton("Химия"))
    markup.add(types.KeyboardButton("История"), types.KeyboardButton("Обществознание"))
    bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Математика", "Русский", "Биология", "География", "Физика", "Химия", "История", "Обществознание"])
def handle_message(message):
    sub_name = {
        "Математика": "Математике",
        "Русский": "Русскому",
        "Биология": "Биологии",
        "География": "Географии",
        "Физика": "Физике",
        "Химия": "Химии",
        "История": "Истории",
        "Обществознание": "Обществознанию"
    }

    data_scores = {
        "Математика": data_based.data_math,
        "Русский": data_based.data_rus,
        "Биология": data_based.data_bio,
        "География": data_based.data_geo,
        "Физика": data_based.data_phiz,
        "Химия": data_based.data_him,
        "История": data_based.data_hist,
        "Обществознание": data_based.data_obsh
    }

    try:
        sub_n = sub_name[message.text]
        subject = message.text
        bot.send_message(message.chat.id, f'Введите свой код для получения результатов по {sub_n}:')
        bot.register_next_step_handler(message, send_results, subject, data_scores)
    except:
        bot.reply_to(message, "Выберите предмет:")
def send_results(message, subject, data_scores):
    code = message.text
    if code.isdigit():
        results = data_based.get_scores(data_scores[subject], int(code))
        bot.send_message(message.chat.id, results)
        bot.send_message(message.chat.id, "Выберите предмет:")
    else:
        handle_message(message)

bot.polling(none_stop=True)
