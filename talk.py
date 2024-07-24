import json
import random


def dict_talk(content):
    with open('data.json', 'r', encoding='utf-8') as f:
        reply = ""
        data = json.load(f)
        words = list(data.keys())
        for i in words:
            if i in content:
                lth = len(data[i])
                r = random.randint(0, lth-1)
                reply = data[i][r]
                break
        return reply
