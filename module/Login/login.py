import time
import os
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


from functools import reduce
'''The package below include VNworks account form:
    username = ...
    password = ...
'''
from mydata import *
# from selenium.webdriver.common.by import By


"""
This test use normal login case.
Please change self.driver path for the successful runtime.
""" 
def handle(driver):
    try:
        feedback2 = driver.find_elements(by=By.CLASS_NAME, value="field-validation-error")
        txt = list(reduce(lambda x, y: x+[y.text], feedback2, []))
        if not txt:
            raise Exception()
    except:
        assert False
    else:
        print(txt)
        assert True
    time.sleep(1)

def handle1(driver):
    try:
        feedback1 = driver.find_element(by=By.CLASS_NAME, value="js__other-errors.re__other-errors.re__show")
        txt = feedback1.text
        if not txt:
            raise Exception()
    except:
        assert False
    else:
        print(txt)
        assert True
    time.sleep(1)

def check_exception(driver):
    driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
    time.sleep(0.3)
    handle(driver)

def check_exception1(driver):
    driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
    time.sleep(0.3)
    handle1(driver)
        

def check_exception_forgot(driver):
    driver.find_element_by_id("button-reset").submit()
    time.sleep(0.3)
    handle(driver)
    

class LoginTesting(unittest.TestCase):
    def setUp(self):
        self.username = username
        self.password = password
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get('https://batdongsan.com.vn/')
        
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(5)
    
    # def test_login_successfull(self):
    #     self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
    #     self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
    #     btnLogin = self.driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        
    #     try:
    #         if self.driver.title == "Kênh thông tin số 1 về bất động sản - Cập nhật mới nhất tháng 11/2021":
    #             raise Exception()
    #         self.driver.find_element(by=By.ID, value="kct_login")
    #         user = self.driver.find_element(by=By.ID, value="UserName")
    #     except:
    #         print(self.driver.title)
    #         feedback = self.driver.find_elements_by_class_name(
    #             "js__btn-login.re__btn.re__btn-pr-solid--md")
    #         print(list(reduce(lambda x, y: x+[y.text], feedback, [])))
    #         assert False
    #     else:
    #         print(self.driver.title)
    #         print("Username " + user.text)
    #         assert True
        

    # def test_login_wrong_pass(self):
    #     self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
    #     self.driver.find_element(by=By.ID, value="Password").send_keys(self.password + "abc")
        
    #     check_exception1(self.driver)     

    # def test_login_wrong_username(self):
    #     self.driver.find_element(by=By.ID, value="UserName").send_keys("lamhuy123@hcmut.edu.vn")
    #     self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
    #     check_exception1(self.driver)

    # def test_login_empty_password(self):
    #     self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
    #     self.driver.find_element(by=By.ID, value="Password").send_keys("")
        
    #     check_exception(self.driver)

    # def test_login_empty_email(self):
    #     self.driver.find_element(by=By.ID, value="UserName").send_keys("")
    #     self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
    #     check_exception(self.driver)

    def test_login_empty_both_2fields(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys("")
        self.driver.find_element(by=By.ID, value="Password").send_keys("")
        
        check_exception(self.driver)
       
    def tearDown(self):
        self.driver.quit()

# class TestLoginWithFb(unittest.TestCase):
#     def setUp(self):
#         self.fbname = fbname
#         self.fbpass = fbpass
#         cService = Service(ChromeDriverManager().install())
#         options = Options()
#         options.add_argument("--log-level=3")
#         self.driver = webdriver.Chrome(options=options, service=cService)
#         # self.driver.implicitly_wait(3)
#         self.driver.maximize_window()
#         print("[Open browser] Open google chrome browser")

#         print("========== [Begin Test] ==========")
#         self.driver.get('https://batdongsan.com.vn/')
#         time.sleep(0.5)
#         first = self.driver.find_element(By.XPATH, "//div[@id='kct_login']//a[@class='js__login-by-facebook-btn.re__btn re__btn-se-border--md.re__btn-icon-left--md.re__form-login-social-btn-facebook']")
#         first.click()
#         time.sleep(2)
#         self.driver.find_element(by=By.CLASS_NAME, value="re__form-login-social-btn-facebook").click()
#         time.sleep(5)

#     def test_login_fb(self):
#         self.driver.find_element(by=By.ID, value="email").send_keys(fbname)
#         self.driver.find_element(by=By.ID, value="pass").send_keys(fbpass)
        
#         btnLogin = self.driver.find_element_by_id("loginbutton").submit()
        
#         if "Kênh thông tin số 1 về bất động sản - Cập nhật mới nhất tháng 11/2021"in self.driver.title:
#             assert True
#         assert False
        
#     def tearDown(self):
#         self.driver.quit()
# class TestLoginWithGG(unittest.TestCase):
#     def setUp(self):
#         self.fbname = fbname
#         self.fbpass = fbpass
#         cService = Service(ChromeDriverManager().install())
#         options = Options()
#         options.add_argument("--log-level=3")
#         self.driver = webdriver.Chrome(options=options, service=cService)
#         # self.driver.implicitly_wait(3)
#         self.driver.maximize_window()
#         print("[Open browser] Open google chrome browser")

#         print("========== [Begin Test] ==========")
#         self.driver.get('https://batdongsan.com.vn/')
#         time.sleep(0.5)
#         self.driver.find_element(by=By.ID, value="kct_login").click()
#         time.sleep(2)
#         self.driver.find_element(by=By.CLASS_NAME, value="re__form-login-social-btn-facebook").click()
#         time.sleep(5)

#     def test_login_fb(self):
#         self.driver.find_element(by=By.ID, value="email").send_keys(fbname)
#         self.driver.find_element(by=By.ID, value="pass").send_keys(fbpass)
        
#         btnLogin = self.driver.find_element_by_id("loginbutton").submit()
        
#         if "Kênh thông tin số 1 về bất động sản - Cập nhật mới nhất tháng 11/2021"in self.driver.title:
#             assert True
#         assert False
        
#     def tearDown(self):
#         self.driver.quit()

if __name__ == '__main__':
    unittest.main()