# Python 3.9
import json
import time
import requests

now = time.localtime()
now_time = time.strftime("%Y-%m-%d %H:%M:%S",now)
# print(now_time)

# 自定义关键词key_word
# key_word = "测试结果："
key_word = "执行时间："

# 你复制的webhook地址
url = "https://open.feishu.cn/open-apis/bot/v2/hook/8942cfa9-b5c7-421d-99c5-9075577dc7eb"

payload_message = {
    "msg_type": "text",
    "content": {
        "text": key_word + now_time
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))

# print(response.text)

