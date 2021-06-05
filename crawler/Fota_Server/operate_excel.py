import os
import zipfile
import pandas as pd
class Local_oprator():
    def __init__(self, active_data_name):
        self.download_path = 'C:/Users/yuhan/Downloads/'
        self.active_data_name = active_data_name

        # target folder
        self.decompress_folder = self.download_path + 'active_data'

    def unzip(self):
        # unzip active data in target folder
        file = zipfile.ZipFile(self.download_path + self.active_data_name + '.zip')
        file.extractall(self.decompress_folder)

        print('//// unzip ', self.active_data_name + ' finished!!!!')

        self.csv_to_excel()

    def create_unzip_folder(self):
        os.mkdir(self.decompress_folder)
        print('decompress folder created')

    def csv_to_excel(self):
        csv_file = pd.read_csv(self.decompress_folder + '/%s.csv' %self.active_data_name)
        csv_file.to_excel('C:/Users/yuhan/Downloads/active_data/%s.xlsx' %self.active_data_name, sheet_name='data')

    # create a depress folder in the same path with zip files: c:/download/
    def operate_local_data(self):
        #if target folder not exists, create it
        if not os.path.exists(self.decompress_folder):
            self.create_unzip_folder()

        #unzip active data in target folder
        self.unzip()










