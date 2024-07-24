import requests
import re

url = "http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/" \
              "57/building_id/283/floor_id/2077/room_id/35543/flag/1"


def elec_inquire():
    resp = requests.get(url)
    balance = re.findall(r'">(.*?)元', resp.text)[0]
    print(balance)
    return balance
