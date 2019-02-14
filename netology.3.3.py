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

    def __and__(self, other):
        params = {
            'access_token': TOKEN,
            'source_uid': self.id,
            'target_uid': other.id,
            'v': '5.92'
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        list_of_friends = []

        for id in response.json()['response']:
            list_of_friends.append(User(id))

        for friend in list_of_friends:
            print(friend)



user1 = User(118021403)
user2 = User(97675040)

user1 & user2