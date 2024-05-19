from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import data_based

# Инициализация бота и диспетчера
bot = Bot(token='6948178394:AAGUR_SnfEIr49ejx-lYNPje3ogLJN-d6yE')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение состояний
class Form(StatesGroup):
    subject = State()  # Состояние для выбора предмета
    code = State()     # Состояние для ввода кода

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add("Математика", "Русский", "Биология", "География",
               "Физика", "Химия", "История", "Обществознание")
    await bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)
    await Form.subject.set()

@dp.message_handler(state=Form.subject)
async def choose_subject(message: types.Message, state: FSMContext):
    subjects = {
        "Математика": "Математике",
        "Русский": "Русскому",
        "Биология": "Биологии",
        "География": "Географии",
        "Физика": "Физике",
        "Химия": "Химии",
        "История": "Истории",
        "Обществознание": "Обществознанию"
    }

    if message.text in subjects:
        await state.update_data(subject=message.text)
        await bot.send_message(message.chat.id, f'Введите свой код для получения результатов по {subjects[message.text]}:')
        await Form.code.set()
    else:
        await bot.send_message(message.chat.id, 'Пожалуйста, выберите предмет из предложенных.')

@dp.message_handler(state=Form.code)
async def get_code(message: types.Message, state: FSMContext):
    code = message.text
    if code.isdigit():
        user_data = await state.get_data()
        subject = user_data['subject']

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

        results = data_based.get_scores(data_scores[subject], int(code))
        await message.answer(results)
        await state.finish()  # Сброс состояния после получения результата
    else:
        await bot.send_message(message.chat.id, 'Пожалуйста, введите числовой код.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
