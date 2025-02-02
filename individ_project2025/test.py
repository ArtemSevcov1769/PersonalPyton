import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# Укажите ваш OpenAI API-ключ
openai.api_key = "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"

# Функция для ответа на сообщения
async def chat_with_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_reply = response.choices[0].message.content
    await update.message.reply_text(bot_reply)

# Основная функция
if __name__ == "__main__":
    # Укажите токен вашего бота
    application = ApplicationBuilder().token("7036308915:AAGwZ3I90LgBG_KfrJiXkhjZWK_JNVxomXY").build()

    # Обработчик сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gpt))

    # Запустите бота
    application.run_polling()