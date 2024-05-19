from aiogram import Bot, Dispatcher, types, executor
import data_based

bot = Bot(token='7036308915:AAGwZ3I90LgBG_KfrJiXkhjZWK_JNVxomXY')
dp = Dispatcher(bot)

subject_selection = {}

@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton("Математика"), types.KeyboardButton("Русский"))
    markup.add(types.KeyboardButton("Биология"), types.KeyboardButton("География"))
    markup.add(types.KeyboardButton("Физика"), types.KeyboardButton("Химия"))
    markup.add(types.KeyboardButton("История"), types.KeyboardButton("Обществознание"))
    await bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)


@dp.message_handler(lambda message: message.text in ["Математика", "Русский", "Биология", "География", "Физика", "Химия", "История", "Обществознание"])
async def select_subject(message: types.Message):
    subject_selection[message.from_user.id] = message.text
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
    sub_n = sub_name[message.text]
    await bot.send_message(message.chat.id, f'Введите свой код для получения результатов по {sub_n}:')


@dp.message_handler(lambda message: message.from_user.id in subject_selection)
async def handle_code(message: types.Message):
    subject = subject_selection[message.from_user.id]
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

    code = message.text
    try:
        await bot.send_message(message.chat.id, data_based.get_scores(data_scores[subject], int(code)))
        await bot.send_message(message.chat.id, 'Выберите предмет')
        del subject_selection[message.from_user.id]
    except:
        await bot.send_message(message.chat.id, 'Неверный код. Попробуйте еще раз.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
