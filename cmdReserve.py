import requests
import re
from elec import elec_inquire
from talk import dict_talk
from eat import what2eat
from draw import lucky_memo
from relay import relay_respond
from iot2 import run

pipe_path = '/tmp/pipe_demo'
api0 = "http://127.0.0.1:3000/post/0"
api1 = "http://127.0.0.1:3000/post/1"
api2 = "http://127.0.0.1:3000/post/2"


def send(api1, group_name, content=""):
    data = {
        'name': group_name,
        'content': content
    }
    try:
        resp = requests.post(api1, data=data)

        resp = resp.json()
        return True
    except:
        return False

def sendpho(api2, group_name, content=""):
    data = {
        'name': group_name,
        'content': content
    }
    try:
        resp = requests.post(api2, data=data)

        resp = resp.json()
        return True#sendpho
    except:
        return False


def withdraw(line):
    line2 = line
    receive = re.findall(r'【(.*?)】', line)
    #print(receive)
    receive.append(line2.split("：",1)[1])
    #print(receive)
    group_name = receive[0]
    user_name = receive[1]
    content = receive[2]
    return group_name, user_name, content

def analyze(group_name, user_name, content):
    if "bang" in content:
        return "bong!"
    if "ping" in content:
        return "pong!"
    if "@GGG" in content:
        if "功能介绍" in content:
            intro = "新功能！\n以下功能均需@到我才能使用：\n\n查询寝室电费：发送“电费”\n\n" \
                    "早午晚吃什么：发送“吃什么”\n\nsteam折扣：发送“steam”\n\n不合口味/想看更多折扣？" \
                    "发送“换一个”！\n\n抽签：看看今日运气！一天仅有一抽，发送“抽签”\n\n" \
                    "闲聊：运气好的话，说不定能触发关键词？"
            return intro
        elif "开门" in content:
            if run():
                return '开门指令已发送！お帰り'
            else:
                return '唔...貌似门锁网断了呢'
        elif "电费" in content:
            reply = "寝室电费余额：" + elec_inquire()
            return reply
        elif "吃什么" in content:
            return relay_respond(user_name,1,0,1)
        elif "吃啥" in content:
            return relay_respond(user_name,1,0,1)
        elif "steam" in content:
            return relay_respond(user_name,1,1,0)
        elif "换一个" in content:
            return relay_respond(user_name,0,0,0)
        elif "抽签" in content:
            return lucky_memo(user_name)
        elif "demo1" in content:
            return 'demo1'
        elif "牢大" in content:
            return 'laoda'
        elif "笑他" in content:
            return 'laoda'
        else:
            return dict_talk(content)
    else:
        return ''

while True:
    with open(pipe_path, 'r') as pipe:
        line = pipe.readline()
        if not line:
            break
        print(line)
        datasheet = withdraw(line)
        reply = analyze(*datasheet)
        if reply == '':
            continue
        elif reply == 'demo1':
            if sendpho(api2,datasheet[0],'/tmp/test.txt'):
                print("向群聊"+datasheet[0]+"发送测试txt成功")
            else:
                print("尝试向群聊"+datasheet[0]+"发送测试txt失败")
        elif reply == 'steam':
            if sendpho(api2,datasheet[0],'/tmp/steamdata.png'):
                print("向群聊"+datasheet[0]+"发送steam数据成功")
            else:
                print("尝试向群聊"+datasheet[0]+"发送steam数据失败")
        elif reply == 'laoda':
            if sendpho(api2,datasheet[0],'/tmp/OIP.jpg'):
                print("向群聊"+datasheet[0]+"发送牢大png成功")
            else:
                print("尝试向群聊"+datasheet[0]+"发送牢大png失败")
        elif reply == 'noMemory':
            reply = "咱忘了你要换什么了..."
            if send(api1, datasheet[0], reply):
                print("向群聊"+datasheet[0]+"发送消息："+reply)
                reply = ""
            else:
                print("尝试向群聊" + datasheet[0] + "发送消息：" + reply+" 失败")
        elif send(api1, datasheet[0], reply):
            print("向群聊"+datasheet[0]+"发送消息："+reply)
            reply = ""
        else:
            print("尝试向群聊" + datasheet[0] + "发送消息：" + reply+" 失败")
            reply = ""

