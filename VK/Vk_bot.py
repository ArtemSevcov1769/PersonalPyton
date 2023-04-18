import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
from wiki import get_article
import Parsing
import starships
hi = ['Привет',
      'Салам Уалейкум',
      'Здравствуй'
      ]
with open("Key.txt") as file:
    token = file.readline()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)
def send_message(resp):
    vk.messages.send(user_id=user_id, random_id=random_id, message=resp)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        print(msg)
        user_id = event.user_id
        random_id = random.randint(1, 10**10)
        if msg == 'привет':
            responce = random.choice(hi)
            send_message(responce)
        elif msg == "планеты":
            responce = Parsing.planet(Parsing.urls)
            send_message(responce)
        elif msg.startswith('-к'):
            val = msg[3:]
            responce = f"{get_course(val)}"
            send_message(responce)
        elif msg == "корабль":
            responce = starships.ship(starships.urls)
            send_message(responce)
        elif msg.startswith("-в"):
            article = msg[2:]
            responce = get_article(article=article)
            send_message(responce)
        else:
            responce = f"неизвестная команда"
            send_message(responce)
