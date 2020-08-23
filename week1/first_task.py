import requests
import datetime


ACCESS_TOKEN = "3aef326f3aef326f3aef326f373a9c13b233aef3aef326f65f9dd63c42bf17d44f02c90"


def calc_age(uid):
    payload1 = {
        'v': '5.71',
        'access_token': [ACCESS_TOKEN],
        'user_ids': [uid]
    }
    id_ = requests.get(f'https://api.vk.com/method/users.get',
                       params=payload1).json()['response'][0]['id']
    payload2 = {
        'v': '5.71',
        'access_token': [ACCESS_TOKEN],
        'user_id': id_,
        'fields': 'bdate'
    }
    friends = requests.get('https://api.vk.com/method/friends.get',
                           params=payload2).json()['response']['items']
    ages = {}
    for friend in friends:
        if 'bdate' not in friend.keys():
            continue
        bdate = friend['bdate'].split('.')
        if len(bdate) == 3:
            age = datetime.datetime.now().year - int(bdate[2])
            ages[age] = ages.setdefault(age, 0) + 1
    res_ = []
    for k, v in ages.items():
        res_.append((k, v))
    res_.sort(key=lambda x: (-x[1], x[0]))
    return res_


if __name__ == '__main__':
    res = calc_age('422331380')
    print(res)
