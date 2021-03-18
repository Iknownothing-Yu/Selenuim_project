# operate header of the main page
from selenium.webdriver import ActionChains
import time

class HeadOperation():
    def __init__(self, broswer):
        self.broswer = broswer

    def chooselanguage(self):
        languageselect = self.broswer.find_element_by_class_name('icon-rebrush-chevron-chevron-up-down')
        ActionChains(self.broswer).move_to_element(languageselect).perform()
        time.sleep(2)
        languageselect.click()
        countrybox = self.broswer.find_element_by_xpath(
            '//div[@class="popover-content"]//span[@class="select2-selection select2-selection--single"]')
        countrybox.click()
        countries = self.broswer.find_elements_by_xpath('//div[@class="popover-content"]//ul/li')
        for country in countries:
            ActionChains(self.broswer).move_to_element(country).perform()
            time.sleep(1)
            if country.text == 'International':
                country.click()
                break