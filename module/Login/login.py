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
        feedback2 = driver.find_elements(by=By.CLASS_NAME, value="js__other-errors.re__other-errors")
        txt = list(reduce(lambda x, y: x+[y.text], feedback2, []))
        if not txt:
            raise Exception()
    except:
        assert False
    else:
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
        time.sleep(15)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(5)
    
    def test_login_successfull(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
        btnLogin = self.driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)
        try:
            check = self.driver.find_elements(by=By.XPATH, value="//div[contains(text(),'Huy Lâm Thành')]")
            if not check:
                raise Exception()
            self.assertTrue(check)
        except:
            assert False
        else:
            assert True
        

    def test_login_wrong_pass(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password + "abc")
        
        check_exception1(self.driver)     

    def test_login_wrong_username(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys("lamhuy123@hcmut.edu.vn")
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
        check_exception1(self.driver)

    def test_login_empty_password(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(by=By.ID, value="Password").send_keys("")
        
        check_exception(self.driver)

    def test_login_empty_email(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys("")
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        
        check_exception(self.driver)

    def test_login_empty_both_2fields(self):
        self.driver.find_element(by=By.ID, value="UserName").send_keys("")
        self.driver.find_element(by=By.ID, value="Password").send_keys("")
        
        check_exception(self.driver)
       
    def tearDown(self):
        self.driver.quit()

class TestLoginWithFB(unittest.TestCase):
    def setUp(self):
        self.fbname = fbname
        self.fbpass = fbpass
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")
        print("========== [Begin Test] ==========")
        self.driver.get('https://batdongsan.com.vn/')
        time.sleep(15)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//body/div[25]/div[1]/div[1]/div[2]/div[1]/a[1]").click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
    def test_login_fb(self):
        self.driver.find_element(by=By.ID, value="email").send_keys(self.fbname)
        self.driver.find_element(by=By.ID, value="pass").send_keys(self.fbpass)
        self.driver.find_element(by=By.NAME, value="login").submit()
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        try:
            check = self.driver.find_elements(by=By.XPATH, value="//a[contains(text(),'Cửa Hang Athena')]")
            if not check:
                raise Exception()
            self.assertTrue(check)
        except:
            assert False
        else:
            assert True
        
    def tearDown(self):
        self.driver.quit()
class TestLoginWithGG(unittest.TestCase):
    def setUp(self):
        self.ggname = "huylamthanh4@gmail.com"
        self.ggpass = "lamhuy213"
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")
        print("========== [Begin Test] ==========")
        self.driver.get('https://batdongsan.com.vn/')
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(2)
        self.driver.find_element(by=By.CLASS_NAME, value="re__btn.re__btn-se-border--md.re__btn-icon-left--md.re__form-login-social-btn-google").click()
        time.sleep(5)
        

    def test_login_gg(self):
        self.driver.find_element(by=By.ID, value="identifierId").send_keys(self.ggname)
        self.driver.find_element(by=By.CLASS_NAME, value="VfPpkd-vQzf8d").click()
        time.sleep(5)
        try:
            check = self.driver.find_elements(by=By.XPATH, value="//span[contains(text(),'Không thể đăng nhập cho bạn')]")
            if not check:
                raise Exception()
            self.assertTrue(check)
        except:
            assert False
        else:
            assert True
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()