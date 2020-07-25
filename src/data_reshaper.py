# data_reshaper.py

import json

if __name__ == '__main__':
    with open('../data/data.json') as json_file:
        old_data = json.load(json_file)

    data = []

    for item in old_data:
        try:
            mobile_speed = item['speed_data']['mobile_speed']
        except:
            mobile_speed = None
        try:
            GNI = item['GNI']
        except:
            GNI = None
        
        data.append(
            {
                'name': item['name'],
                'region': item['region'],
                'population': item['population'],
                'internet_users': item['internet_users'],
                'penetration': item['penetration'],
                'users_region': item['users_region'],
                'facebook_subs': item['facebook_subs'],
                'broadband_speed': item['speed_data']['broadband_speed'],
                'mobile_speed': mobile_speed,
                'GNI': GNI
            }
        )

    print(data[0])

    with open('../data/new_data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)