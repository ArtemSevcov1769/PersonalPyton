import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from test import get_scores
with open("Key.txt") as file:
    token = file.readline()
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)

def send_message(resp):
    random_id = random.randint(1, 10**10)
    vk.messages.send(user_id=user_id, random_id=random_id, message=resp)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        msg = event.text.lower()
        print(msg)
        print(type(msg))
        try:
            resp = get_scores(int(msg))
            send_message(resp)
        except:
            if msg == 'география':
                resp = ''
                send_message(resp)
