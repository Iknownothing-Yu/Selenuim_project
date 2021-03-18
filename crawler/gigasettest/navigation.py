# operate navigation bar of the main page
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from crawler.gigasettest.accessories import AccOperation

class NaviOperation():
    def __init__(self, broswer):
        self.broswer = broswer
        self.accessoriesoperate = AccOperation(self.broswer)  # accessories page object
        self.wait = WebDriverWait(self.broswer, 10)

    def test_nav_menu(self):
# move mouse on to navigation, click Zubehör, get into Zubehör page scroll down to bottom, get back to the main page
        mainmenu = self.broswer.find_element_by_class_name('b_nav__menu-item--nav-1')
        acc = self.broswer.find_element_by_xpath(
            '//ul[@class="b_nav__menu b_nav__menu--level0"]/li[@data-category-id="category-node-126"]/a')
        ActionChains(self.broswer).move_to_element(mainmenu).perform()  # mouse move on to main menu
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                               '//ul[@class="b_nav__menu b_nav__menu--level0"]/li[@data-category-id="category-node-126"]/a')))  # wait for the present of product list
        ActionChains(self.broswer).move_to_element(acc).click().perform()  # click Zubehör
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'b_product-list-toolbar')))  # wait for the last row of products presented
        self.accessoriesoperate.scrollpage() # operate accessories page

# search bar search product GX290
    def test_gx290page(self):
        searchbar = self.broswer.find_element_by_class_name('b_header-functions__search-button')
        searchbar.click()
        self.broswer.find_element_by_name('q').send_keys('GX290')  # search GX290 in search bar
        time.sleep(3)  # it is important to wait for a while. if not the hidden elements will not be displayed
        # autocompletejs = 'arguments[0].style.display="block";'
        resultcontainer = self.broswer.find_element_by_id('search_autocomplete')
        resultlist = resultcontainer.find_elements_by_tag_name('li')
        result = resultlist[1].find_element_by_tag_name('a')
        result.click()
        return
