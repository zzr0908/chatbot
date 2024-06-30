from flask import Flask, request
import requests
import json
import random
from openai import OpenAI
import os

app = Flask(__name__)
key = "sk-b1cbb8207ef94ea58517d38392040eb7"


@app.route('/')
def hello_world():
    return '在此输入apikey 样式:sk-s5S5BoV...'


@app.route('/message',methods = ['POST'])
def mess():  # put application's code here
    message = request.json.get('msg')
    api_key = "sk-b1cbb8207ef94ea58517d38392040eb7"
    client = OpenAI(api_key=key, base_url="https://api.deepseek.com")
    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response)
    # messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
    res = {
        "resmsg": response,
        "code": 200
    }
    return res


if __name__ == '__main__':
    app.run(threaded=False,processes=5, host="0.0.0.0", port="8080")


