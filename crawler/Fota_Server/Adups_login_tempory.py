from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from Selenuim_project.crawler.Fota_Server.download_IMEI import DownloadTable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# new changes
class LoginPage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mg.adups.cn/ota/login.jsp")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)


    def login(self):
        engpage = self.driver.find_elements_by_xpath('//form[@id = "login"]//p[@class = "login-p"]//font[@class = "login-font2"]/a')[1]
        engpage.click()
        self.un = 'Gigaset'
        self.pw = 'Gigaset#001'
        self.username = self.driver.find_element_by_id('userName')
        self.username.send_keys(self.un)
        self.passowrd = self.driver.find_element_by_id('passWord')
        self.passowrd.send_keys(self.pw)
        time.sleep(10)
        self.submit = self.driver.find_element_by_id('subId')
        self.submit.click()
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'confirm-exit')))
        self.alert = self.driver.find_element_by_id('confirm-exit')

        return

if __name__ == '__main__':
    ob = LoginPage()
    ob.login()
    time.sleep(6)
    imeitable = DownloadTable(ob.driver)
    imeitable.project_details()
    time.sleep(4)
    imeitable.get_IMEItable()





