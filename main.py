from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random

token = "abcda71211a601e294531a51b50afaf8bee94afb736184bc08828960c6118cee2d816909255e9179aa5a6"
vk_session = vk_api.VkApi(token=token)


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                print(event.user_id)
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'ВЫсаси', 'random_id': 0})