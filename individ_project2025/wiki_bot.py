import telebot, wikipedia, re

bot = telebot.TeleBot('7680947557:AAEW2rTbLt62GnRaTTr7ld_fIjhwJqyqMR8')
wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите любое слово, чтобы узнать, что это такое!')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == "привет":  # Проверяем, содержит ли сообщение "привет"
        bot.send_message(message.chat.id, "Привет, я помогу найти информацию о всём!")
    else:
        bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)
