import time
from steam import get_steam
from t2p import steam2image
from eat import what2eat


def relay_respond(user, isFirst, isSteam, isEat):
    try:  # 0.timestamp1.username2.command3.i
        with open('relay.txt', 'r') as f:
            relay_history = f.read()
            history = relay_history.split('\n')
    except FileNotFoundError:
        with open('relay.txt', 'w') as f:
            f.write('')
    with open('relay.txt', 'r+') as f:
        full = f.read()
        if isFirst:
            if isSteam:
                get_steam(1)
                steam2image()
                f.seek(0, 0)
                f.write(f'{time.time()},{user},steam,1\n'+full)
                return 'steam'
            elif isEat:
                f.seek(0, 0)
                f.write(f'{time.time()},{user},eat\n'+full)
                return what2eat()
        else:
            for j in history:  # 循环行
                data = j.split(',')
                if user in j:  # 匹配用户历史
                    if time.time() - float(data[0]) <= 6000:  # 10分钟内
                        if data[2] == 'steam':
                            i = int(data[3])
                            i += 6
                            get_steam(i)
                            steam2image()
                            f.seek(0, 0)
                            f.write(f'{time.time()},{user},steam,{i}\n'+full)
                            return 'steam'
                        elif data[2] == 'eat':
                            f.seek(0, 0)
                            f.write(f'{time.time()},{user},eat\n'+full)
                            return what2eat()
                    else:
                        return 'noMemory'
                else:
                    return 'noMemory'

