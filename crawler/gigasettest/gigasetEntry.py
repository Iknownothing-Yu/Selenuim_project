# find Elements in root-shadow with JS
# ActionChans
# Gigaset Webseite eintreten, Fenster vergrößern
# Datenschutz akzeptieren
# Elemente in Navigation manupulieren: searchbar Zubehör suchen, Seite nach unten&oben ziehen, Sprache wechseln, Produkt
# herausfinden
# comments added
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from crawler.gigasettest.navigation import NaviOperation
from crawler.gigasettest.head import HeadOperation

class MainPage:
    # initial, config
    def setUp(self):
        self.broswer = webdriver.Chrome()
        self.wait = WebDriverWait(self.broswer, 10)
        url = 'https://www.gigaset.com/de_de/'
        # create a Http connection
        self.broswer.get(url)
        self.broswer.maximize_window()
        time.sleep(2)
        self.headoperate = HeadOperation(self.broswer) # head object
        self.navoperate = NaviOperation(self.broswer)
        print('-------------')
        return

# find elements in root-shadow pop up (shadow dom)
    def selectcookies(self):
        ele = self.broswer.find_element_by_id('usercentrics-root')  # find the parent of root-shadow
        shadowroot = self.broswer.execute_script('return arguments[0].shadowRoot',
                                                 ele)  # excute out root-shadow node and locate it
        self.footer = shadowroot.find_element_by_tag_name('footer')  # locate any element in root-shadow
        self.settingbutton = self.footer.find_elements_by_tag_name('button')[0].click()

# if there is an alert popup after getting into main page, click to cancel it
        # wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="onesignal-slidedown-dialog"]//div[@id="slidedown-footer"]/button[@id="onesignal-slidedown-cancel-button"]')))
        # a = broswer.find_element_by_xpath('//div[@id="onesignal-slidedown-dialog"]//div[@id="slidedown-footer"]/button[@id="onesignal-slidedown-cancel-button"]')
        # a.click()
        return

    def test_mainpage(self):
        self.navoperate.test_nav_menu()
        self.headoperate.chooselanguage() # choose language
        time.sleep(1)
        self.navoperate.test_gx290page()

op = MainPage()
op.setUp()
time.sleep(2)
op.selectcookies()
time.sleep(3)
op.test_mainpage()



