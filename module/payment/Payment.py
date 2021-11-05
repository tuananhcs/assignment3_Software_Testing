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


"""
This test use normal login case.
Please change self.driver path for the successful runtime.
""" 

class PaymentTesting(unittest.TestCase):
    def setUp(self):
        self.username="huy.lam2214@hcmut.edu.vn"
        self.password="Lamhuy213"
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get('https://batdongsan.com.vn/')
        time.sleep(1)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value="UserName").send_keys(self.username)
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        btnLogin = self.driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)
    # def test1(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys("30000")
    #     self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("30000")
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(5)
    #     aler1 = self.driver.switch_to.alert.accept() 
    #     assert True
    # def test2(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.ID, value="txtMoney").send_keys("300")
    #     self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("30000")
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(5)
    #     aler1 = self.driver.switch_to.alert.accept() 
    #     assert True
    # def test3(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.ID, value="txtMoney").send_keys("3000")
    #     # Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")        
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(5)
    #     aler1 = self.driver.switch_to.alert.accept() 
    #     assert True
    # def test4(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys("300")
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
        # Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys(
        #     "abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")    
    #     time.sleep(5)
    #     aler1 = self.driver.switch_to.alert.accept() 
    #     assert True
    # def test5(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys("30000")
    #     Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
    #     self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(5)
    #     try:
    #         fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
    #         self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Bạn nhập mã an toàn không hợp lệ")
    #     except:
    #         print(self.driver.title)
    #         assert False
    #     finally:
    #         print(fieldValidator.text)
    #         assert True
    # def test6(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(2)
    #     self.driver.find_element(by=By.ID, value="txtMoney").send_keys("900000000")
    #     time.sleep(2)
    #     Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
    #     self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(2)
    #     try:
    #         fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
    #         self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Số tiền bạn nhập nhỏ hơn 10.000")
    #     except:
    #         print(self.driver.title)
    #         assert False
    #     finally:
    #         print(fieldValidator.text)
    #         assert True
    # def test7(self):
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys("300")
    #     self.driver.find_element(by=By.ID, value="btnSave").click()
    #     time.sleep(5)
    #     aler1 = self.driver.switch_to.alert.accept() 
    #     assert True
    # def test8(self):
        # self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        # time.sleep(5)
        # self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        # time.sleep(2)
        # self.driver.find_element(by=By.ID, value="txtMoney").send_keys("900000000")
        # time.sleep(2)
        # Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
        # self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
        # self.driver.find_element(by=By.ID, value="btnSave").click()
        # time.sleep(2)
        # try:
        #     fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
        #     self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Bạn không được nhập số tiền lớn hơn 100.000.000")
        # except:
        #     print(self.driver.title)
        #     assert False
        # finally:
        #     print(fieldValidator.text)
        #     assert True
    def test9(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("100.2")
        time.sleep(2)
        Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
        self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(2)
        try:
            fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Số tiền bạn nhập nhỏ hơn 10.000")
        except:
            print(self.driver.title)
            assert False
        finally:
            print(fieldValidator.text)
            assert True

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()