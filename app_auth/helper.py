from django.conf import settings
import json
import os
import platform

def PriceJson():
    try:
        if platform.system() == 'Linux':
           json_file = open (settings.BASE_DIR, 'PROJECT/static/price.json')
        else:
           json_file = open (settings.BASE_DIR, 'PROJECT\\static\\json\\price.json')
        data1 = json.load (json_file)
        json_file.close ()
        # print(data1)
        return data1['data']
    except Exception as e:
        print ("Error reading json file", e)
        return []