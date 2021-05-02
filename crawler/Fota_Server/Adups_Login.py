from selenium import webdriver
from collections import defaultdict
from selenium.webdriver.support import wait
import time
from PIL import Image
import pytesseract

class LoginPage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mg.adups.cn/ota/login.jsp")
        self.driver.maximize_window()
        wait.WebDriverWait(self.driver, 5)

    def get_threshold(self, img):
        pixel_dict = defaultdict(int)

        # 像素及该像素出现次数的字典
        rows, cols = img.size
        for i in range(rows):
            for j in range(cols):
                pixel = img.getpixel((i, j))
                pixel_dict[pixel] += 1

        count_max = max(pixel_dict.values())  # 获取像素出现出多的次数
        pixel_dict_reverse = {v: k for k, v in pixel_dict.items()}
        threshold = pixel_dict_reverse[count_max]  # 获取出现次数最多的像素点

        return threshold

    def get_bin_table(self, threshold):
        # 获取灰度转二值的映射table
        table = []
        for i in range(256):
            rate = 0.1  # 在threshold的适当范围内进行处理
            if threshold * (1 - rate) <= i <= threshold * (1 + rate):
                table.append(1)
            else:
                table.append(0)
        return table

    def remove_noise(self, img):

        rows, cols = img.size  # with and hight of the image
        noise_position = []  # position of noises

        # Traverse all the point of the image and cut the edge of the image
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                # pixel_set用来记录该point附近的黑色像素的数量
                pixel_set = []
                # 取该点的邻域为以该点为中心的九宫格
                for m in range(i - 1, i + 2):
                    for n in range(j - 1, j + 2):
                        if img.getpixel((m, n)) != 1:  # 1为白色,0位黑色
                            pixel_set.append(img.getpixel((m, n)))

                # 如果该位置的九宫内的黑色数量小于等于4，则判断为噪声
                if len(pixel_set) <= 4:
                    noise_position.append((i, j))

        # 对相应位置进行像素修改，将噪声处的像素置为1（白色）
        for pos in noise_position:
            img.putpixel(pos, 1)

        return img

    def getVerificationCodeImg(self):
        self.driver.save_screenshot('/image1.png')
        imglocation = self.driver.find_element_by_id('validateCodeImg').location
        #print(imglocation)

        x_left = imglocation['x'] * 1.25
        y_top = imglocation['y'] * 1.25
        x_right = x_left + 100 * 1.25
        y_buttom = y_top + 30 * 1.25

        code_img = Image.open('/image1.png')
        code_img = code_img.crop((x_left, y_top, x_right, y_buttom))
        code_img = code_img.convert('L')
        code_img.save('/image2.png')

        threshold = self.get_threshold(code_img)
        bin_table = self.get_bin_table(threshold)
        out = code_img.point(bin_table, '1')
        de_noise = self.remove_noise(out)

        '''
        w, h = code_img.size
        #print(w, h)
        img_matrix = code_img.load()


        for y in range(h):
            for x in range(w):
                if img_matrix[x, y] < threshold:
                    img_matrix[x, y] = 0
                else:
                    img_matrix[x, y] = 255

        return code_img
        '''
        return de_noise

    '''
    # delete noise around code 
    def delete_spot(self):
        images = self.getVerificationCodeImg()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                        # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        return images
        '''

    def getVerificationCode(self):
        #code_img = self.delete_spot()
        code_img = self.getVerificationCodeImg()
        code = pytesseract.image_to_string(code_img)
        # 去掉识别结果中的特殊字符
        exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
        text = ''.join([x for x in code if x not in exclude_char_list])
        return code

    def login(self):
        un = 'Gigaset'
        pw = 'Gigaset#001'
        username = self.driver.find_element_by_id('userName')
        username.send_keys(un)
        passowrd = self.driver.find_element_by_id('passWord')
        passowrd.send_keys(pw)
        loginbutton = self.driver.find_element_by_id('subId')
        loginbutton.click()

ob = LoginPage()
print(ob.getVerificationCode())

























