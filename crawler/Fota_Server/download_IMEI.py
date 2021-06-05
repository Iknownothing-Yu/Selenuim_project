from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import os
from Selenuim_project.crawler.Fota_Server.operate_excel import Local_oprator as OpExcel
class DownloadTable():
    def __init__(self, adupsdriver):
        self.driver = adupsdriver
        self.downlod_path = 'C:/Users/yuhan/Downloads'
        self.wait = WebDriverWait(self.driver, 120, 4)
        self.suffix = ['crdownload', 'tmp']

    def project_details(self):
        self.left_nav_items = self.driver.find_elements_by_xpath('//div[@id = "menu"]/ul[@class = "accordion"]/li')

        #print(len(self.left_nav_items))
        self.user_detail = self.left_nav_items[2]
        self.user_detail.find_element_by_tag_name('div').click()
        #find project details
        time.sleep(3)
        self.user_detail_submenu = self.user_detail.find_element_by_tag_name('ul')

        # important to change display to block
        self.driver.execute_script('arguments[0].style.display = "block";', self.user_detail_submenu)
        self.user_detail_itms = self.user_detail_submenu.find_elements_by_tag_name('li')
        self.project_detail = self.user_detail_itms[-1]
        self.project_detail.click()

    def get_IMEItable(self):
        self.driver.switch_to_frame('home')
        time.sleep(5)
        self.projects_table = self.driver.find_element_by_xpath('//div[@id = "result"]/table/tbody')
        self.project_list = self.projects_item = self.projects_table.find_elements_by_tag_name('tr')
        #self.total_project = len(self.project_list)
        for i in range(3):
            self.projects_item = self.project_list[i].find_elements_by_tag_name('td')[-1]
            # self.projects_item = self.projects_table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[-1]
            self.projects_item.find_element_by_tag_name('a').click()
            self.load_imei = self.projects_item.find_element_by_tag_name('ul').find_elements_by_tag_name('li')[2]

            # click Export IMEI button to download IMEI table
            self.driver.execute_script('arguments[0].click();', self.load_imei)

            # Start download detected
            self.wait.until(lambda driver: self.begin_load(self.load_imei))
            print('------begin download----------')
            time.sleep(2)
            self.find_download_file_index(i + 1)
            time.sleep(2)
            # End download detected
            self.wait.until(lambda driver: self.end_load())
            print('------end download-------------')
            self.op_excel = OpExcel(self.file_name)
            # if no such file then create new one
            self.op_excel.operate_local_data()


    #get the state of begining download: "color" of font. the font color changes to blue when download begining
    def begin_load(self, element):
        #print(element.value_of_css_property("color"))
        if element.value_of_css_property("color") == "rgba(47, 160, 236, 1)":
            return True
        else:
            return False

    # find the downloaded file index in the Download, only need to search the first n files
    # n: find the first n element in download file. the value is i in get_IMEItable(self)
    # file_name: the name of current downloading file. the value is  in get_IMEItable(self)
    def find_download_file_index(self, n):
        self.file_list = os.listdir(self.downlod_path)[:n]
        #print(self.file_list, 'status 1')  status1 confirms the file begins to download
        for i in range(n):
            if self.file_list[i].split('.')[-1] in self.suffix:
                self.file_index = i
                self.file_name = self.file_list[i].split('.')[0]
                break
        #print('the current downloaded file is : ', self.file_list[self.file_index], '---------- index:', self.file_index)

    # get the state of ending download: the suffix of the last downloaded file isn't "crdownload"
    def end_load(self):
        self.file_list = os.listdir(self.downlod_path)[:self.file_index + 1]

        #print(self.file_list, 'status 2')   status2 stays there until the download is ended

        # if suffix of the current file is "crdownload" or "tmp", it means the file is downloading
        if self.file_list[self.file_index].split('.')[-1] in self.suffix:
            print(self.file_name, 'is downloading......')
            return False
        else:
            #get downloaded active data name
            return True
























