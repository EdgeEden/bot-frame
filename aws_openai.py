import requests

urltxt = 'http://13.208.249.182:5000/post'
urlpho = 'http://13.208.249.182:5000/pho'

def openai_cli(model,question,isPho):
    if isPho:
        url = urlpho
    else:
        url = urltxt
    payload = {'model': model, 'question': question}
    resp = requests.post(url, data=payload)
    print(resp.text)
    print(model)
    print(resp.status_code)
    return resp.text

