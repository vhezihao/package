import requests
import json
from com.api.demo.timestamp import get_current_time
from com.api.demo.add_account import add_account


## ------------------ 获取 13 位时间戳 ------------------
current_time = get_current_time()
print(current_time)

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjU3MjcyNTE5LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.xbyjfk_VKmlPFIbB8Kmskb9ACAq1D-lReefWDA1peJ_Z36UviwxFxXyOElHZd7BGGxk__iDPQC-rrzEkbkURsX1Kr5xuT22GGx6MdfWXcVk9ia8e1N1bwwyOmNoQMsoGuJmJCupYPeuJV0_W-b-0w2GP-dR7DV-8S9Th-RJVnMe7x7nUydBaoOGaIk_n3q5OHCnBClpCtxu5Eht5WmiqlRi1WFG5LtHyTdzR6YqvGzqwETGgC-ASF9FIYqEHA5pEiWuT7PtCzuWbYrXehw2ihxcVUZ58VzYS33MQIFkciRmAYiKtfE7jYqNiKAOqtcn6kRdX5UrSP47-Sw-5BKjVIQ'

uid_list = [2290592065425666]

for uid in uid_list:
  url = "https://boss-proxy-test.ihago.cn/boss_proxy/ymicro/api?group_id=863&method=Add"

  cookies = {'username': 'dw_hezihao','yyuid': '73378', 'jwt': token}
  # payload = "{\"uid\":107112776,\"token\":\"username=dw_hezihao; yyuid=73378; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjUzNjE1NzI4LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.KCX9V67zLH2BNZnFAJT7_EKNYN6VOxGMcbAdBE4JZ7YIbwZUG2Cvxe8kZsFkOd2RUKWRG5g3_-_3FFEstwQBuFbTiw-3K97hYCbJctr7KSOsn9faTQx4YrBu2iGIe8_azl60ZoQSC0BbIQ21RzqrSkKBoOlTXtbwqCi2_OhuLjHMCQ0XwAOVUgKYX1rtdEZUDX9o5CYKZbOtN0N19WoEmeaER6_-26jO-BvOn8z6ZVjYjPokHA-VHcIxpppG_ZCV0HykHmTANDmB62sSH3AicV7J_JUBcbsHsdgSk8FNhDPn68Sdxo9JiJXkO6y3wplFqrkYk2s4pdT7jbU7EbezPw\",\"sequence\":1653049835270}"
  payload ={"uid": uid,"token": "username=dw_hezihao; yyuid=73378; jwt=" + token,"sequence": current_time}

  headers = {
    'content-type': 'application/json',
    # 'cookie': 'username=dw_hezihao; yyuid=73378; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjUzNjE1NzI4LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.KCX9V67zLH2BNZnFAJT7_EKNYN6VOxGMcbAdBE4JZ7YIbwZUG2Cvxe8kZsFkOd2RUKWRG5g3_-_3FFEstwQBuFbTiw-3K97hYCbJctr7KSOsn9faTQx4YrBu2iGIe8_azl60ZoQSC0BbIQ21RzqrSkKBoOlTXtbwqCi2_OhuLjHMCQ0XwAOVUgKYX1rtdEZUDX9o5CYKZbOtN0N19WoEmeaER6_-26jO-BvOn8z6ZVjYjPokHA-VHcIxpppG_ZCV0HykHmTANDmB62sSH3AicV7J_JUBcbsHsdgSk8FNhDPn68Sdxo9JiJXkO6y3wplFqrkYk2s4pdT7jbU7EbezPw',
    'x-ymicro-api-method-name': 'Token.Add',
    'x-ymicro-api-service-name': 'net.ihago.testenv.srv.token'
  }

  response = requests.request("POST", url, headers=headers, json=payload,cookies=cookies)

  print(response.text)

