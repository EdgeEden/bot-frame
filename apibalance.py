import requests
from datetime import datetime


def balance():
        url = 'https://api.chatanywhere.org/v1/query/balance'
        headers = {
            'Authorization': 'sk-11pupwZDwi5A3VEn9QiCzJhWaU24stb50tzc2fLICoSqEyQj'
            }
        resp = requests.post(url, headers=headers)
        data = resp.json()
        today = datetime.today().date()
        specified_date = datetime.strptime('2024-05-17', '%Y-%m-%d').date()
        days_diff = (today - specified_date).days
        used = data['balanceUsed']
        total = data['balanceTotal']
        avaliable = total - used
        average = used / days_diff
        day = avaliable / average
        return "已用余额：%f\n可用余额：%f\n预计可用%d天" % (used, avaliable, day)

