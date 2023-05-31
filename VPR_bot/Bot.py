import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
import data_based

with open("Key.txt") as file:
    token = file.readline()
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)
def get_but(text, color):
    return{
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }
keyboard = {
    "one_time": False,
    "buttons": [
        [get_but("Математика", 'positive'), get_but("Русский", 'positive')],
        [get_but("привет", 'positive'), get_but("пока", 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

class Result:
    def __init__(self, object, data_based):
        self.object = object
        self.data_b = data_based
    def get_result(self):
        send_message(f'Введите свой код для получения результатов по {self.object}:')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == peer_id:
                msg = event.text.lower()
                if msg[0].isdigit() and 5 <= int(msg[0]) <= 8:
                    send_message(data_based.get_scores(self.data_b, int(msg)))
                    send_message('Выберите предмет')
                    break

rus = Result('русскому языку', data_based.data_rus)
math = Result('математике', data_based.data_math)
# def rus():
#     send_message('Введите свой код для получения результатов по русскому языку:')
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == peer_id:
#             msg = event.text.lower()
#             if msg[0].isdigit() and 5 <= int(msg[0]) <= 8:
#                 send_message(data_based.get_scores(data_based.data_rus, int(msg)))
#                 break
#             elif 'мат' in msg:
#                 math()
#                 return
#             elif 'рус' in msg:
#                 send_message('Введите свой код для получения результатов по русскому языку:')
#                 continue
#             else:
#                 send_message('Неизвестный запрос. Введите "математика" для математики или "русский" для русского языка')
#                 continue
# def math():
#     send_message('Введите свой код для получения результатов по математике:')
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == peer_id:
#             msg = event.text.lower()
#             if msg[0].isdigit() and 5 <= int(msg[0]) <= 8:
#                 send_message(data_based.get_scores(data_based.data_math, int(msg)))
#             elif 'рус' in msg:
#                 rus()
#                 return
#             elif 'мат' in msg:
#                 send_message('Введите свой код для получения результатов по математике:')
#                 continue
#             else:
#                 send_message('Неизвестный запрос. Введите "математика" для математики или "русский" для русского языка')
#                 continue


def send_message(resp):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': resp, 'random_id': 0, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        peer_id = event.user_id
        msg = event.text.lower()
        if 'рус' in msg:
            rus.get_result()
        elif 'мат' in msg:
            math.get_result()
        else:
            pass

