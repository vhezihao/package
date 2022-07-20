import uiautomator2 as u2
import json
import time

# d = u2.connect('c6e989d7')
d = u2.connect_usb('42c90697')

# try:
#     d.app_stop("com.yy.hiyo")
# except:
#     pass

# print(d.info)
# print(json.dumps(d.info,indent=4,ensure_ascii=False))

# d.app_start("com.yy.hiyo") # 启动APP

# d.app_stop("com.ss.android.ugc.aweme")  #停止应用

# d(resourceId="com.yy.hiyo:id/tv_search").click() #点击搜索按钮
# d(className="android.widget.TextView").click() #点击搜索按钮
# d(description="").click() #点击搜索按钮
# d.xpath('//*[@resource-id="com.yy.hiyo:id/tv_search"]').click() #点击搜索按钮
# d(text="Search").click()  #text定位
for i in range(5):
    d.swipe(0.915, 0.371, 0.081, 0.371, 0.3)
    time.sleep(2)


