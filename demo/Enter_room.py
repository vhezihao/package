import requests
import json
from com.api.demo.get_cid import search_cid
from com.api.demo.get_token import get_token
import time

# token = 'AXLQcjzuW8UNDGK2UtyT00XAADr1PKysu0tX0jgnQ1XZ1qwTVaqyoUxwHMLc8KxjE44qu4TP6OU%3D%2CnNM9ovMxw682OVUaAW8EpAsKCU8vEG5aDH%2FvauBxIEB1o5VZbaqNhWX72HOXqMxMRxaNNbVgMMifx7PMjSwFnYUuZ%2FSpWWb7Ug%2FX%2FqOdqPq3EVLt6WMhzi1ruffYLn5q3CMpUOtf8LogpgnT5NHldfdnxhL8gmON70emPYWUV3A%3D'
# uid = '2295032954568560'

# token_list =[
#     "4LPKIOPsUGpcTSRxTOAzOWD0%2BAqrJYqADKRkvIfeWI%2BFto7Q9ESJcCsm9TQK6ZOM8M9%2BK3kssAo%3D%2CnNM9ovMxw682OVUaAW8EpOhLUHVkZoQEBkG86vfagwyiBU%2BD4RLmwpg%2BnYgP%2F8wyWX7NzpA1GCJLm%2FipqlTl18M%2FjM4xtdbDvqdoT5H%2BH5L5J47jkULE9SSBQ29ReRuY86xb%2BlUkolOGyjVGnuAE1VQPjb%2BiMR1uiPjl4obU1YY%3D",
#     "l2dfZfSphvH%2Ff%2F7g9tFGQFSYQnuVPJqhAc2wSX6UwOA9NVsugKnxgqIpz2kNvs%2FBYfFWT01ggWk%3D%2CnNM9ovMxw682OVUaAW8EpAsKCU8vEG5aDH%2FvauBxIEB1o5VZbaqNhfYIAMcO%2FsyVNBH4FfUlIumP0WgRceOm21r77l9YX6vkk20QpiUHQJwl16pRspUpZ%2B87xsQhRZsezGSrfSG%2FsRKAnoHnQAOWOJ5gPMS44NQsC4SgqHW5wZM%3D",
#     "qZ2168jC8c52nPgrxP4prUX7aDcsm3jvsfUjH0YavdvEUM83a4pyP0TPyoxOE3KWtQp1oaO43w0%3D%2CnNM9ovMxw682OVUaAW8EpGz7vXLMr4ABcuX6fSXrJgbysey8c5ecxt9Dz6Tvb96DeYEfoEM0qcX2Bwy0muG%2F6Sl8bPVEDMUaYu%2FD8VBn1Gt5itB1JavvLwiPgSGqo%2B%2F3YMfmKE9GJmM59Z09iGQJbO5xZ2oSt38AD8V8UhLcv8E%3D",
#     "SgeMVsWMI1gIrjiyEPliFBdLUFI6FghD2AnThHF48fScLsq0JRDZ5EBi44jJqbM7hkwXnFKZU2c%3D%2CnNM9ovMxw682OVUaAW8EpO8p%2FrHMZR37%2Fcz5zyjQEMv2aRa%2BwA3G%2F7P0Tfx4%2F%2BmHOm7DZRLhPCEGuTsfcV9VGx%2BMMD%2F4n8hBriqzU7gzN%2BCma0i5f2JevvbsJYHZAOWJX97pvMaBTqnQMAghT6As9rDfnXVfqlBy8rFDGe2wATI%3D",
#     "N0sgo0QFb1%2FnXumYj2kbhodX95qWbaVzGFoUuEDni%2F%2BHrgknk66%2FeOt02zZ8BAvdWwy0CG1A4mo%3D%2CnNM9ovMxw682OVUaAW8EpCbcmELu8nas1gTLngdyvTQmvNz6DyzjyBthKMBi7HQxYrpjH%2BD8XEUeSgn55ZrJvAn0v9Ck1Kio8%2FylNrCIFzlJO3DfUXKc0N6%2BVuJHSGqv3kADHdloZBuJUuXHNVjRkcIUXI%2B9XK1KtzFFXTQPQmY%3D"
# ]
#
# uid_list=[2295032954568500,2295032954568560,2295032954568570,2295032954568580,2295032954568590]

token_list, uid_list = get_token()
print('token_list:', json.dumps(token_list, indent=4, ensure_ascii=False))
print('uid_list:', json.dumps(uid_list, indent=4, ensure_ascii=False))

# cid = search_cid()
# cid_list =['C_1540226775869561172_V1_AE_881_AE', 'C_1540223232055974228_V1_AE_881_AE', 'C_1540246653389278760_V1_AE_881_AE', 'C_1540259013738908740_V1_AE_881_AE', 'C_1540259025013197892_V1_AE_881_AE']

cid_list = search_cid()
print('cid_list:', json.dumps(cid_list, indent=4, ensure_ascii=False))

def Enter_room():
    for uid,token,cid in zip(uid_list,token_list,cid_list):
          # print(uid,token,cid)
          # dera 中东正式
          url = f"https://i-894.ihago.net/ymicro/api?token={token}{uid}"
          # print('', json.dumps(url, indent=4, ensure_ascii=False))

          payload = json.dumps({
            # "cid": "C_1540226775869561172_V1_AE_881_AE",
            "cid": cid,
            "password": ""
          })
          headers = {
            'x-ymicro-api-method-name': 'Channel.Enter',
            'x-ymicro-api-service-name': 'net.ihago.channel.srv.mgr',
            'x-auth-token': str(token),
            'x-app-ver': '50000',
            'Content-Type': 'application/json'
          }

          response = requests.request("POST", url, headers=headers, data=payload)

          # print('', json.dumps(headers, indent=4, ensure_ascii=False))
          print(response.text)


def Leave_room():
    for uid, token, cid in zip(uid_list, token_list, cid_list):
        url = f"https://i-894.ihago.net/ymicro/api?token={token}"

        payload = json.dumps({
            "cid": cid,
            "min_base": False
        })
        headers = {
            'x-ymicro-api-method-name': 'Channel.Leave',
            'x-ymicro-api-service-name': 'net.ihago.channel.srv.mgr',
            'x-auth-token': str(token),
            'x-app-ver': '50000',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


def robot():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
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
    print('发送到机器人成功')


if __name__ == '__main__':
    # 退房
    Leave_room()

    time.sleep(5)

    # 进房
    # Enter_room()

    # 机器人
    robot()

