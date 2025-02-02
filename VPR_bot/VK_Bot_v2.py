import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
import data_based

with open("Key.txt") as file:
    token = file.readline().strip()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)

def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + text + "\"}",
            "label": text
        },
        "color": color
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

sub_name = {
    "математика": "Математике",
    "русский": "Русскому",
    "биология": "Биологии",
    "география": "Географии",
    "физика": "Физике",
    "химия": "Химии",
    "история": "Истории",
    "обществознание": "Обществознанию"
}

data_scores = {
    "математика": data_based.data_math,
    "русский": data_based.data_rus,
    "биология": data_based.data_bio,
    "география": data_based.data_geo,
    "физика": data_based.data_phiz,
    "химия": data_based.data_him,
    "история": data_based.data_hist,
    "обществознание": data_based.data_obsh
}

user_state = {}

def send_message(peer_id, message, keyboard=None):
    vk_session.method('messages.send', {
        'peer_id': peer_id,
        'message': message,
        'random_id': 0,
        'keyboard': keyboard
    })

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        peer_id = event.user_id
        msg = event.text.lower()

        if msg in sub_name:
            user_state[peer_id] = {'subject': msg}
            send_message(peer_id, f'Введите код, чтобы узнать результат по {sub_name[msg]}')
        elif peer_id in user_state and msg.isdigit():
            subject = user_state[peer_id]['subject']
            code = int(msg)
            results = data_based.get_scores(data_scores[subject], code)
            send_message(peer_id, results)
            del user_state[peer_id]  # Удаляем состояние пользователя после обработки
        else:
            send_message(peer_id, 'Пожалуйста, выберите предмет из списка ниже.', keyboard=keyboard)
