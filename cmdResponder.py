import requests
import re
import time
from elec import elec_inquire
from talk import dict_talk
from eat import what2eat
from draw import lucky_memo
from relay import relay_respond
from iot2 import run
from iot3 import check
from systate import system_stat
from kimi import kimi
from lolicon import setu
from aws_openai import openai_cli
from apibalance import balance
from ghchart import chart

pipe_path = '/tmp/pipe_demo'
api1 = "http://127.0.0.1:3000/post/1"
api2 = "http://127.0.0.1:3000/post/2"
model = "gpt-3.5-turbo"
isPho = False

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
    global model
    global isPho
    if "bang" in content:
        return "bong!"
    if "ping" in content:
        return "pong!"
    if "espDown" in content:
        return "门锁掉线，请检查网络或拔插门锁芯片喵"
    if "\state" in content:
        if check():
            reply = system_stat()+'\n门锁在线'
            return reply
        else:
            reply = system_stat()+'\n门锁离线'
            return reply
    if "/state" in content:
        if check():
            reply = system_stat()+'\n门锁在线'
            return reply
        else:
            reply = system_stat()+'\n门锁离线'
            return reply
    if "/开门" in content or "\开门" in content:
        if run():
            return '开门指令已发送！お帰り'
        else:
            return '唔...貌似门锁掉线了呢'
    if "@GGG" in content:
        content = content.replace('@GGG','')
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
                return '唔...貌似门锁掉线了呢'
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
        elif "热力图" in content or "频率图" in content:
            return chart(content)
        elif "色图" in content:
            return setu(content)
        elif "涩图" in content:
            return setu(content)
        elif "key余额" in content:
            return balance()
        elif "传图" in content:
            isPho = True
            reply = '收到~下次ai请求将会传递最近的聊天图片'
            return reply
        elif "gpt3" in content:
            model = "gpt-3.5-turbo"
            back = "AI切换为"+str(model)
            return back
        elif "gpt4" in content:
            model = "gpt-4o"
            back = "AI切换为"+str(model)
            return back
        else:
            try:
                reply = openai_cli(model,content,isPho)#dict_talk
                isPho = False
                return reply
            except:
                isPho = False
                return "ai请求到达上限了喵~管理员没钱充值，请一分钟后再试"
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
            if sendpho(api2,datasheet[0],'/tmp/chatimg.jpg'):
                print("向群聊"+datasheet[0]+"发送测试jpg成功")
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
        elif reply == 'svg_success':
            if sendpho(api2,datasheet[0],'/tmp/chart.png'):
                print("向群聊"+datasheet[0]+"发送表图成功")
            else:
                print("向群聊"+datasheet[0]+"发送表图失败")
        elif reply == 'Success':
            if sendpho(api2,datasheet[0],'/tmp/setu.jpg'):
                print("向群聊"+datasheet[0]+"发送涩图成功")
            else:
                print("向群聊"+datasheet[0]+"发送涩图失败")
        elif reply == 'Keyword_Error':
            reply = "找不到对应关键词的图片...唔"
            if send(api1, datasheet[0], reply):
                print("向群聊"+datasheet[0]+"发送消息："+reply)
            else:
                print("尝试向群聊" + datasheet[0] + "发送消息：" + reply+" 失败")
        elif reply == 'Network_Error':
            reply = "网络连接不畅...没法发送图片呢"
            if send(api1, datasheet[0], reply):
                print("向群聊"+datasheet[0]+"发送消息："+reply)
            else:
                print("尝试向群聊" + datasheet[0] + "发送消息：" + reply+" 失败")
        elif send(api1, datasheet[0], reply):
            print("向群聊"+datasheet[0]+"发送消息："+reply)
            reply = ""
        else:
            print("尝试向群聊" + datasheet[0] + "发送消息：" + reply+" 失败")
            reply = ""
    time.sleep(1)
