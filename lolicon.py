import requests
import re

url = 'https://api.lolicon.app/setu/v2?r18=2'


def setu(content):
    keyword = re.search(r'\((.*?)\)', content)
    if keyword is not None:
        tag = keyword.group(1)
        url_get = url + "&tag=" + tag
    else:
        url_get = url
    res = requests.get(url_get)
    data = res.json()
    try:
        url_pic = data['data'][0]['urls']['original']
    except IndexError:
        return "Keyword_Error"
    try:
        img = requests.get(url_pic).content
    except:
        return "Network_Error"
    with open('/tmp/setu.jpg', 'wb') as fp:
        fp.write(img)
    return "Success"



