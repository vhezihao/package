import requests
from com.api.demo.timestamp import get_current_time


for i in range(1000):
    current_time = get_current_time()
    # print("时间戳",current_time)

    # url = "https://i-test-863.ihago.net/ymicro/sapi?method=LotteryV2.Draw&sname=net.ihago.money.api.promote3dprops&X-Lang=zh&X-App-Ver=0&X-OsType=android&X-Os-Ver=&hago-seq-id=1653548494297&_method=LotteryV2.Draw"
    #
    # payload = "{\"sequence\":1653548494295,\"pool_id\":\"pool1\",\"combo\":1,\"version\":28165,\"consume_type\":3}"
    # headers = {
    #   'cookie': ' hd_newui=0.9413952481998826; _ga=GA1.2.1428288227.1621322210; hiido_ui=0.8684642180971247; uaasCookie=AgFor%2F25m77%2B40ZjN9fMupGPF61Hp4sL3IRO64Q%2FlQJfZVz6jnGzU3yl%2Bwu7u3Yl%2CMt1hAhhplzmS3790mpPSrqi7JwmAz2yLYYJGnxhsVOqFJqR5HXdOBP%2FKlUu9o6nFvBaR8bs84%2FS0nU2WR5tdfI39lkc84lSGbmh3qlJMo8T%2FIEVNoEKljQ5fpVMkIutvCEQItwKvqXj7DT%2F6R07IGTe041s35hDAJl1RroJyh8sXusxJc0Vfj9wbcdIgMVYoJWvNCq2qM8b5WFecUZAJR0KHKsE4tYNeA5wHSXVtNRwwU93%2FrY6HjvBoGP%2BUiLT%2BtE%2BXF1Op4PffQZUNltq6b8suhicbrpoiGnEirgg5arx5RYjhRLtvG88MSFCw5GZx; hagouid=107062396',
    #   'Content-Type': 'text/plain'
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # print(response.text)

    # url = "https://boss-proxy-test.ihago.cn/boss_proxy/ymicro/api?group_id=863&method=Add"
    url = "https://i-test-863.ihago.net/ymicro/sapi?method=LotteryV2.Draw&sname=net.ihago.money.api.promote3dprops&X-Lang=zh&X-App-Ver=0&X-OsType=android&X-Os-Ver=&hago-seq-id=1653548494297&_method=LotteryV2.Draw"

    cookies = {'hd_newui': '9413952481998826', '_ga': 'GA1.2.1428288227.1621322210','hiido_ui': '0.8684642180971247','hagouid': '107062396',
               'uaasCookie': 'AgFor%2F25m77%2B40ZjN9fMupGPF61Hp4sL3IRO64Q%2FlQJfZVz6jnGzU3yl%2Bwu7u3Yl%2CMt1hAhhplzmS3790mpPSrqi7JwmAz2yLYYJGnxhsVOqFJqR5HXdOBP%2FKlUu9o6nFvBaR8bs84%2FS0nU2WR5tdfI39lkc84lSGbmh3qlJMo8T%2FIEVNoEKljQ5fpVMkIutvCEQItwKvqXj7DT%2F6R07IGTe041s35hDAJl1RroJyh8sXusxJc0Vfj9wbcdIgMVYoJWvNCq2qM8b5WFecUZAJR0KHKsE4tYNeA5wHSXVtNRwwU93%2FrY6HjvBoGP%2BUiLT%2BtE%2BXF1Op4PffQZUNltq6b8suhicbrpoiGnEirgg5arx5RYjhRLtvG88MSFCw5GZx'}

    # hd_newui=0.9413952481998826; _ga=GA1.2.1428288227.1621322210; hiido_ui=0.8684642180971247; uaasCookie=AgFor%2F25m77%2B40ZjN9fMupGPF61Hp4sL3IRO64Q%2FlQJfZVz6jnGzU3yl%2Bwu7u3Yl%2CMt1hAhhplzmS3790mpPSrqi7JwmAz2yLYYJGnxhsVOqFJqR5HXdOBP%2FKlUu9o6nFvBaR8bs84%2FS0nU2WR5tdfI39lkc84lSGbmh3qlJMo8T%2FIEVNoEKljQ5fpVMkIutvCEQItwKvqXj7DT%2F6R07IGTe041s35hDAJl1RroJyh8sXusxJc0Vfj9wbcdIgMVYoJWvNCq2qM8b5WFecUZAJR0KHKsE4tYNeA5wHSXVtNRwwU93%2FrY6HjvBoGP%2BUiLT%2BtE%2BXF1Op4PffQZUNltq6b8suhicbrpoiGnEirgg5arx5RYjhRLtvG88MSFCw5GZx; hagouid=107062396
    # payload = "{\"uid\":107112776,\"token\":\"username=dw_hezihao; yyuid=73378; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjUzNjE1NzI4LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.KCX9V67zLH2BNZnFAJT7_EKNYN6VOxGMcbAdBE4JZ7YIbwZUG2Cvxe8kZsFkOd2RUKWRG5g3_-_3FFEstwQBuFbTiw-3K97hYCbJctr7KSOsn9faTQx4YrBu2iGIe8_azl60ZoQSC0BbIQ21RzqrSkKBoOlTXtbwqCi2_OhuLjHMCQ0XwAOVUgKYX1rtdEZUDX9o5CYKZbOtN0N19WoEmeaER6_-26jO-BvOn8z6ZVjYjPokHA-VHcIxpppG_ZCV0HykHmTANDmB62sSH3AicV7J_JUBcbsHsdgSk8FNhDPn68Sdxo9JiJXkO6y3wplFqrkYk2s4pdT7jbU7EbezPw\",\"sequence\":1653049835270}"
    payload = {"sequence": current_time,
               "pool_id": 'pool1',
               "combo": 1,
               "consume_type": 3,
               "version": 28203}

    headers = {
      # 'cookie': ' hd_newui=0.9413952481998826; _ga=GA1.2.1428288227.1621322210; hiido_ui=0.8684642180971247; uaasCookie=AgFor%2F25m77%2B40ZjN9fMupGPF61Hp4sL3IRO64Q%2FlQJfZVz6jnGzU3yl%2Bwu7u3Yl%2CMt1hAhhplzmS3790mpPSrqi7JwmAz2yLYYJGnxhsVOqFJqR5HXdOBP%2FKlUu9o6nFvBaR8bs84%2FS0nU2WR5tdfI39lkc84lSGbmh3qlJMo8T%2FIEVNoEKljQ5fpVMkIutvCEQItwKvqXj7DT%2F6R07IGTe041s35hDAJl1RroJyh8sXusxJc0Vfj9wbcdIgMVYoJWvNCq2qM8b5WFecUZAJR0KHKsE4tYNeA5wHSXVtNRwwU93%2FrY6HjvBoGP%2BUiLT%2BtE%2BXF1Op4PffQZUNltq6b8suhicbrpoiGnEirgg5arx5RYjhRLtvG88MSFCw5GZx; hagouid=107062396',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload, cookies=cookies)

    # print(response.text)