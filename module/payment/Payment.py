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
        self.maxfield="abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
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
        self.driver.find_element(by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(by=By.ID, value="Password").send_keys(self.password)
        self.driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)
    def testXYZ1(self):
        """Correct all field"""
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("30000")
        self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("30000")
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        try:
            fieldValidator = self.driver.switch_to.alert
            self.assertTrue(fieldValidator.text == "B???n c???n nh???p m?? an to??n")
            fieldValidator.accept()
        except:
            assert False
        finally:
            assert True
    def testXYZ2(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("300")
        self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("30000")
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        try:
            fieldValidator = self.driver.switch_to.alert
            self.assertTrue(fieldValidator.text == "B???n c???n nh???p m?? an to??n")
            fieldValidator.accept()
        except:
            assert False
        finally:
            assert True
    def testXYZ3(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("3000")   
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        try:
            fieldValidator = self.driver.switch_to.alert
            self.assertTrue(fieldValidator.text == "B???n c???n nh???p m?? an to??n")
            fieldValidator.accept()
        except:
            assert False
        finally:
            assert True
    def testXYZ4(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("300")
        Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys(self.maxfield)    
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        try:
            fieldValidator = self.driver.switch_to.alert
            self.assertTrue(fieldValidator.text == "B???n c???n nh???p m?? an to??n")
            fieldValidator.accept()
        except:
 
            assert False
        finally:

            assert True
    def testXYZ5(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("30000")
        Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
        self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        try:
            fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "B???n nh???p m?? an to??n kh??ng h???p l???")
        except:
            assert False
        finally:
            assert True
    def testXYZ6(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("abc")
        time.sleep(2)
        Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
        self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(2)
        try:
            fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "S??? ti???n b???n nh???p nh??? h??n 10.000")
        except:
            assert False
        finally:
            assert True
    def testXYZ7(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("300")
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(5)
        aler1 = self.driver.switch_to.alert.accept() 
        assert True
    def testXYZ8(self):
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html[1]/body[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="txtMoney").send_keys("900000000")
        time.sleep(2)
        Amount = self.driver.find_element(by=By.ID, value="txtOrderDescription").send_keys("abc")  
        self.driver.find_element(by=By.ID, value="secode").send_keys("ABCE")  
        self.driver.find_element(by=By.ID, value="btnSave").click()
        time.sleep(2)
        try:
            fieldValidator = self.driver.find_element(by=By.CLASS_NAME, value="errormessage")
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "B???n kh??ng ???????c nh???p s??? ti???n l???n h??n 100.000.000")
        except:
            assert False
        finally:
            assert True
    def testXYZ9(self):
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
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "S??? ti???n b???n nh???p nh??? h??n 10.000")
        except:
            assert False
        finally:
            assert True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()