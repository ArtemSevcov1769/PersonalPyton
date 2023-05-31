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
        [get_but('Математика', 'secondary'), get_but('Русский', 'secondary'), get_but('Биология', 'secondary'), get_but('География', 'secondary')],
        [get_but('Физика', 'secondary'), get_but('Химия', 'secondary'), get_but('История', 'secondary'), get_but('Обществознание', 'secondary')],
        [get_but('Назад(главное меню)', 'negative')]

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
                elif 'рус' in msg:
                    rus.get_result()
                elif 'мат' in msg:
                    math.get_result()
                elif 'био' in msg:
                    bio.get_result()
                elif 'гео' in msg:
                    geo.get_result()
                elif 'ист' in msg:
                    hist.get_result()
                elif 'общ' in msg:
                    obsh.get_result()
                elif 'физ' in msg:
                    phiz.get_result()
                elif 'хим' in msg:
                    him.get_result()
                elif 'наз' in msg:
                    send_message('Выберите предмет')
                    break
                else:
                    break

rus = Result('русскому языку', data_based.data_rus)
math = Result('математике', data_based.data_math)
bio = Result('биологии', data_based.data_bio)
geo = Result('географии', data_based.data_geo)
hist = Result('истории', data_based.data_hist)
obsh = Result('обществознанию', data_based.data_obsh)
him = Result('химии', data_based.data_him)
phiz = Result('физике', data_based.data_phiz)

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
        elif 'био' in msg:
            bio.get_result()
        elif 'гео' in msg:
            geo.get_result()
        elif 'ист' in msg:
            hist.get_result()
        elif 'общ' in msg:
            obsh.get_result()
        elif 'физ' in msg:
            phiz.get_result()
        elif 'хим' in msg:
            him.get_result()
        else:
            continue