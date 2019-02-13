# from urllib.parse import urlencode
# APP_ID = 6858428
# AUTH_URL = 'https://oauth.vk.com/authorize'
# auth_data = {
#     'client_id': APP_ID,
#     'display': 'page',
#     'scope': 'friends,offline',
#     'response_type': 'token',
#     'v': '5.92'
# }
#print('?'.join((AUTH_URL, urlencode(auth_data))))

import requests
import json
TOKEN = 'b759f7c046868edeb57b6360e3b507fef5d425a1b34c681de0d378a9fadbc08db9c552f02f968b221ad91'


class User():
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return 'http://vk.com/id{}'.format(self.id)


def get_friends(u1, u2):
    us1 = ''
    us2 = ''
    for user in list_of_users:
        if user[0] == u1:
            us1 = user[1]
    for user in list_of_users:
        if user[0] == u2:
            us2 = user[1]
    if us1 != '' and us2 != '':
        params = {
            'access_token': TOKEN,
            'source_uid': us1.id,
            'target_uid': us2.id,
            'v': '5.92'
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        list_of_friends = []

        for id in response.json()['response']:
            list_of_friends.append(User(id))

        for friend in list_of_friends:
            print(friend)
    else:
        print('Один из пользователей не найден')



user1 = User(118021403)
user2 = User(97675040)
list_of_users = ['user1', user1], ['user2', user2]


inputted_str = ''
while inputted_str != 'stop':
    print('Вот список доступных пользователей:')
    for user in list_of_users:
        print(user[0])
    inputted_str = input('Введите двух пользователей в формате user1 & user2 или stop ')
    if inputted_str != 'stop':
        splitted_str = inputted_str.split(' ')
        try:
            if splitted_str[1] == '&':
                get_friends(splitted_str[0], splitted_str[2])
            else:
                print('Неверная команда')
        except IndexError:
            print('Неверная команда (IndexError)')
        except KeyError:
            print('Пользователь не найден')
print('Работа программы завершена')
