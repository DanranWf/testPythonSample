from selenium import webdriver
from userInfo import username, password
from selenium.webdriver.support.wait import WebDriverWait
# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import base64
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

# 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['-enableautomation'])
driver = webdriver.Chrome(options=options)


class LoginBiLiBiLi(object):
    def __init__(self):
        self.url = "https://passport.bilibili.com/login"
        self.driver = driver
        self.username = username
        self.password = password
        self.username_loc = ("id", "login-username")
        self.password_loc = ("id", "login-passwd")
        self.login_button_loc = ("class name", "btn-login")
        self.slider_button_loc = ("class name", "geetest_slider_button")
        self.wait = WebDriverWait(self.driver, 10)
        self.a=6

    def input_username(self):
        """
        username
        :return:
        """
        located = self.wait.until(ec.presence_of_element_located(self.username_loc))
        located.send_keys(self.username)
        print(a)

    def input_password(self):
        """
        password
        :return:
        """
        located = self.wait.until(ec.presence_of_element_located(self.password_loc))
        located.send_keys(self.password)

    def click_login(self):
        """
        click
        :return:
        """
        located = self.wait.until(ec.presence_of_element_located(self.login_button_loc))
        located.click()

    def get_slider_button(self):
        """
        
        :return:
        """
        return self.wait.until(ec.presence_of_element_located(self.slider_button_loc))

    # def get_pic(self):
        """
        
        :return:
        """
        # 
        filename = ["full.png", "bg.png"]
        className = ["geetest_canvas_fullbg", "geetest_canvas_bg"]
        # 
        for i in range(len(className)):
            js = f"var change = document.getElementsByClassName('{className[i]}');return change[0].toDataURL('image/png');"
            im_info = self.driver.execute_script(js)
            data = im_info.split(",")[1]
            data = base64.b64decode(data)
            with open(filename[i], "wb") as f:
                f.write(data)

    def get_gap(self, image1, image2):
        """
        
        :param image1: 
        :param image2: 
        :return:
        """
        # 
        left = 0
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    # 
                    left = i
                    return left

    def is_pixel_equal(self, image1, image2, x, y):
        """
        
        :return:
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]

        threshold = 10  # 允许的像素偏差为10
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def move_to_gap(self, slider, left):
        """
        
        :return:
        """
        # 
        left = left - 9
        ActionChains(self.driver).click_and_hold(slider).perform()
        # 
        ActionChains(self.driver).move_by_offset(xoffset=left - 30, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=25, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=5, yoffset=0).perform()
        sleep(0.6)
        # 
        ActionChains(self.driver).release().perform()

    def login_success(self):
        """
        
        :return:
        """
        try:
            res = self.wait.until(
                ec.text_to_be_present_in_element(("css selector", "div.mini-vip.van-popover__reference"), "大会员"))
            return res
        except Exception:
            return False

    def login(self):
        """
        
        :return:
        """
        # 
        self.driver.get(self.url)
        # 
        self.input_username()
        # 
        self.input_password()
        # 
        self.click_login()
        # 
        sleep(3)
        # self.get_pic()
        
        # image1 = Image.open("full.png")
        # image2 = Image.open("bg.png")
        # left = self.get_gap(image1, image2)
        # slider = self.get_slider_button()
        # self.move_to_gap(slider, left)

        if self.login_success():
            print("成功")
            self.driver.quit()
        else:
            print("失败,再试一次")
            self.login()


if __name__ == '__main__':
    login = LoginBiLiBiLi()
    login.login()
