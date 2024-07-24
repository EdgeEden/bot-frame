import random
from datetime import date
import json
import os


def lucky_memo(user):
    if not os.path.exists('luck_draw.json'):
        history = {}
    else:
        with open('luck_draw.json', 'r', encoding='utf-8') as f:    # 文件存在则内容不应为空
            history = json.loads(f.read())

    if  not history or history['date']!=date.today().__str__():    # 文件为空或日期不对
        history = {'date': date.today().__str__(),
                    user: draw()}
    elif history.get(user) is None: # user今天未抽
        history[user] = draw()
    else:   # 今日已抽
        reply = f'{user} 今日已抽签！\n 今日运势： {history[user]}\n{explain(history[user])}'
        return reply

    reply =f'{user} 今日运势： {history[user]}\n{explain(history[user])}'
    with open('luck_draw.json', 'w', encoding='utf-8') as f:
            json.dump(history, f)
    return reply

def draw():
    tickets = ['上吉', '大吉', '中吉', '小吉', '末吉']
    luck = random.choice(tickets)
    return luck

def explain(res):
    if res == '上吉':
        return "平心正直，理顺则宽，圣无私语，终有分明。此签晧月当空之象，万事光明通达。"
    elif res == '大吉':
        return "任君无疑，路有亨通，随心自在，逍遥得意。此签万事先凶后吉也。"
    elif res == '中吉':
        return "讼终自理，病得安痊，出入求谋，古井逢泉。此签凡事贵人成就也。"
    elif res == '小吉':
        return "浮云遮月，还需疑惑，等到云散，便见明月。此签凡事昏迷未定也。"
    elif res == '末吉':
        return "若得人愁，何时可伸，好言不信，守旧待时。此签鸟投林巢之象，凡事宜忍耐，终应心也，宜耐守已。"


if __name__ == '__main__':
    lucky_memo('tmf')
