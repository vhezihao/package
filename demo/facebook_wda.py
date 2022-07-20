import wda
import time

# c = wda.Client('http://127.0.0.1:8100')
c = wda.USBClient('00008030-0011550221E0802E',port=8100,wda_bundle_id='com.facebook.WebDriverAgentRunner.xctrunner')



# c.session().app_activate('com.apple.Preferences')
# s = c.session().app_activate('com.pkgame.enterprise.hago')
c.session().app_activate('com.pkgame.enterprise.hago')


# c(className='XCUIElementTypeStaticText').click()
# c(name='Search').click()
# c(value='Search').click()
# c(label='Search').click()
# c(className='XCUIElementTypeStaticText',name='Search').click()
# c(xpath='//Table/Other[1]/Image[1]/StaticText[1]').click()
for i in range(5):
    c.swipe(0.915, 0.371, 0.081, 0.371,duration=0.5)
    time.sleep(2)