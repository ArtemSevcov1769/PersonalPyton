from aiogram import Bot, Dispatcher, types, executor
import data_based

bot = Bot('6948178394:AAGUR_SnfEIr49ejx-lYNPje3ogLJN-d6yE')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton("Математика"), types.KeyboardButton("Русский"))
    markup.add(types.KeyboardButton("Биология"), types.KeyboardButton("География"))
    markup.add(types.KeyboardButton("Физика"), types.KeyboardButton("Химия"))
    markup.add(types.KeyboardButton("История"), types.KeyboardButton("Обществознание"))
    await bot.send_message(message.from_user.id, 'Выберите предмет:',
                           reply_markup=markup)  # Используйте bot.send_message


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
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
        await bot.send_message(message.chat.id, f'Введите свой код для получения результатов по {sub_n}:')  # Используйте bot.send_message
        # Используйте lambda для передачи аргументов в send_results
        dp.register_message_handler()
    except:
        await bot.send_message(message.chat.id, 'Выберите свой предмет')  # Исправьте на message.message_id

async def send_results(message, subject, data_scores):
    code = message.text
    if code.isdigit():
        results = data_based.get_scores(data_scores[subject], int(code))
        await message.answer(message.chat.id, results)
    else:
        await handle_message(message)  # Повторно вызовите handle_message, если код неверен


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
