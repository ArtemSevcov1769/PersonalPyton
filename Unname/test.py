import random, vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='vk1.a.juE4Z-Uz4UhNWL53llfBsnGyO0UXdqZGxmtdJdk_0d65wTzcszh-e1MlO6z3auCCDNANpzv8cHbwpxOBLmn4cdon-PFa1O6d6dK6-DOaFwCzJ49xg46ZfZpmQJl4uUdQ7krSZmkZCdPyHFDDj3V9fynJU7CzcRSMLNTBs8noHbuIRjWbgA9yNSTVYRzvQh8or4JOpT0VEqG2mHmvYOGpJw')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 219717133)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=еще_раз_ID_группы")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = (''),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = (''),
                    ts=(''),
                    random_id = get_random_id(),
              	    message='Привет!',
            	    chat_id = event.chat_id
                    )
        if 'Клавиатура' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard = keyboard.get_keyboard(),
                    key = (''),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = (''),
                    ts=(''),
                    random_id = get_random_id(),
              	    message='Держи',
             	    chat_id = event.chat_id
            	    )
'''
for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу']
        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = 'Привет)',
                    random_id = get_random_id()
                    )
        vars2 = ['Клавиатура', 'клавиатура']
        if event.text in vars2:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard.get_keyboard(),
                    message = 'Держи'
                    )
'''