# operate accessories page
import time
from selenium.webdriver import ActionChains
#from crawler.gigasettest.gigasetPopup import MainPage as MP

class AccOperation():
    def __init__(self, broswer):
        self.broswer = broswer

    def scrollpage(self):
        for down in range(20):
            js = 'window.scrollBy(0,100)'
            self.broswer.execute_script(js)
            time.sleep(0.2)
        for up in range(20):
            js = 'window.scrollBy(0,-100)'
            self.broswer.execute_script(js)
            time.sleep(0.2)
        return

'''
    def scrollpage(self):
        scrolldown = 'arguments[0].scrollIntoView(false);'
        scrollup = 'window.scrollTo(window.pageXOffset, 0)'
        self.broswer.execute_script(scrolldown, self.broswer.find_element_by_id('newsletter-subscribe'))  # scroll dowm
        time.sleep(2)
        self.broswer.execute_script(scrollup)  # scroll up
        time.sleep(2)
        self.broswer.back()  # back to main page
        return
'''

