import requests
import re
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

url = 'https://ghchart.rshah.org/'


def chart(content):
    user = re.search(r'\((.*?)\)',content)
    if user is not None:
        tag = user.group(1)
        url_get = url + tag
    else:
        url_get = 'https://ghchart.rshah.org/EdgeEden'
    try:
        res = requests.get(url_get)
    except:
        return "Network_Error"
    with open('chart.svg', 'w') as fp:
        fp.write(res.text)
    pic = svg2rlg('chart.svg')
    renderPM.drawToFile(pic, '/tmp/chart.png', fmt='PNG')
    return "svg_success"
