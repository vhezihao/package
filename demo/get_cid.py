import requests
import json
from com.api.demo.get_uid import func

# uids = func()
# print(uids)

def search_cid():
    # uids = [
    #         '2295032954568500',
    #         '2295032954568560',
    #         '2295032954568570',
    #         '2295032954568580',
    #         '2295032954568590',
    #         '2295032954568690',
    #         '2295032954568700',
    #         # '2295032954568710',
    #         '2295032954568730',
    #         '2295032954568740'
    #        ]

    uids = func()

    cid_list = []

    for uid in uids:
        # 印尼测试
        # url = f"https://i-test-863.ihago.net/anchor_monitor/my_channel?uid={uid}&pageSize=100&pageNum=1"
        # 迪拜正式
        url = f"https://i-881.ihago.net/anchor_monitor/my_channel?uid={uid}&pageSize=100&pageNum=1"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        res = json.loads(response.text)

        # print(json.dumps(res, indent=4, ensure_ascii=False))
        # print(res)

        cid = res['data']["my_own_chan_list"][1]['cid']
        cid_list.append(cid)

    # print(cid_list)
    # print(json.dumps(cid_list,indent=4,ensure_ascii=False))


    #打印出来如 "2295032954568500": "C_1540226775869561172_V1_AE_881_AE"
    # cid_dict = dict(zip(uids, cid_list))
    # print(cid_dict)
    # print(json.dumps(cid_dict,indent=4,ensure_ascii=False))

    # 仅返回房间列表
    return cid_list



if __name__ == '__main__':
    search_cid()



## json 数据转换成 python 字典
# res = json.dumps(json.loads(response.text),indent=4,ensure_ascii=False)



##### 循环获取 json 里面的 key
# cid_list = []
# for item in my_own_chan_list:
#     cid_list.append(item['cid'])
#
# print(cid_list)






