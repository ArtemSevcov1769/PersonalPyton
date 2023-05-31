import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import data_based

with open("Key.txt") as file:
    token = file.readline()
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)

def rus():
    send_message('Введите свой код')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == user_id:
            msg = event.text.lower()
            if msg :
                send_message(data_based.get_scores(data_based.data_rus, int(msg)))
                return
            if msg == 'математика':
                math()
                return
            elif msg == 'русский':
                continue
            else:
                send_message('Неизвестный запрос. Введите "математика" для математики или "русский" для русского языка')
                continue

def math():
    send_message('Введите свой код')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == user_id:
            msg = event.text.lower()
            if msg:
                send_message(data_based.get_scores(data_based.data_math, int(msg)))
                return
            elif msg.find('рус') != -1:
                rus()
                return
            elif 'мат' in msg:
                continue
            else:
                send_message('Неизвестный запрос. Введите "математика" для математики или "русский" для русского языка')
                continue


def send_message(resp):
    random_id = random.randint(1, 10**10)
    vk.messages.send(user_id=user_id, random_id=random_id, message=resp)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        msg = event.text.lower()
        if msg == 'русский':
            rus()
        elif msg == 'математика':
            math()
