import os
import zipfile
import pandas as pd
class Local_oprator():
    def __init__(self, active_data_name):
        self.download_path = 'C:/Users/yuhan/Downloads/'
        self.active_data_name = active_data_name

        # target folder
        self.decompress_folder = self.download_path + 'active_data'

    def decompress_zip(self):
        # unzip active data in target folder
        file = zipfile.ZipFile(self.download_path + self.active_data_name + '.zip')
        file.extractall(self.decompress_folder)

        print('//// unzip ', self.active_data_name + ' finished!!!!')

    # create a depress folder in the same path with zip files: c:/download/
    def create_depress_folder(self):
        #if target folder not exists, create it
        if not os.path.exists(self.decompress_folder):
            os.mkdir(self.decompress_folder)
            print('decompress folder created')

        #unzip active data in target folder
        self.decompress_zip()

    def oprate_csv(self):
        csv_file = pd.read_csv('C:/Users/yuhan/Downloads/active_data/' + self.active_data_name + '.csv')
        csv_file.to_excel('C:/Users/yuhan/Downloads/active_data/1.xlsx', sheet_name='data')








