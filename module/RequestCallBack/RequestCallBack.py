from re import S, match
import time
import os
import re
from typing import Match
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DetailedEstimate(unittest.TestCase):
    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get("https://batdongsan.com.vn/nha-dat-ban")

    def pressSubmit(self):
        buttonSubmit = self.driver.find_element(By.XPATH, './/button[@data-callback="onSubmit_FrontEnd_Product_Details_ContactBox_SendRequest"]')
        buttonSubmit.click()

    def fillForm(self, senderName, senderMobile, senderEmail, senderContext):
        self.driver.find_element(By.NAME, "txtSenderName").send_keys(senderName)
        self.driver.find_element(By.NAME, "txtSenderMobile").send_keys(senderMobile)
        self.driver.find_element(By.NAME, "txtSenderEmail").send_keys(senderEmail)
        self.driver.find_element(By.NAME, "txtSenderContent").send_keys(senderContext)
        self.pressSubmit()

    def clearForm(self):
        self.driver.find_element(By.NAME, "txtSenderName").clear()
        self.driver.find_element(By.NAME, "txtSenderMobile").clear()
        self.driver.find_element(By.NAME, "txtSenderEmail").clear()
        self.driver.find_element(By.NAME, "txtSenderContent").clear()


    def functionAccess(self):
        first = self.driver.find_element(By.XPATH, "//div[@id='product-lists-web']//a[@class='js__product-link-for-product-id']")
        first.click()
        btnCallBack = self.driver.find_element(By.LINK_TEXT, "Yêu cầu liên hệ lại")
        btnCallBack.click()
        time.sleep(5)


    def test_input_name(self):
        self.functionAccess()
        self.fillForm("aa", "0123456789", "aaa@gmail.com", "aaa")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)
    
    def test_no_input_name(self):
        self.functionAccess()
        self.fillForm("", "0123456789", "aaa@gmail.com", "aaa")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)
    
    def test_valid_phonenumber(self):
        self.functionAccess()
        self.fillForm("aaa", "0706665088", "aaa@gmail.com", "aaa")
        check = False
        for x in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)

    def test_invalid_phonenumber(self):
        self.functionAccess()
        self.fillForm("aaa", "706665088", "aaa@gmail.com", "aaa")
        for x in range(1,100):
            time.sleep(0.1)
            message = self.driver.find_elements(By.ID, "validateFortxtSenderMobile")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)

    def test_hotline_phonenumber(self):
        self.functionAccess()
        self.fillForm("aaa", "1900088816", "aaa@gmail.com", "aaa")
        for x in range(1,100):
            time.sleep(0.1)
            message = self.driver.find_elements(By.ID, "validateFortxtSenderMobile")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)

    def test_string_in_phonenumber(self):
        self.functionAccess()
        self.fillForm("aaa", "abc", "aaa@gmail.com", "aaa")
        for x in range(1,100):
            message = self.driver.find_elements(By.ID, "validateFortxtSenderMobile")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)

    def test_no_input_phonenumber(self):
        self.functionAccess()
        self.fillForm("aaa", "", "aaa@gmail.com", "aaa")
        for x in range(1,100):
            time.sleep(0.1)
            message = self.driver.find_elements(By.ID, "validateFortxtSenderMobile")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)          

    def test_valid_email(self):
        self.functionAccess()
        self.fillForm("aa", "0123456789", "aaa@gmail.com", "aaa")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)   

    def test_invalid_email(self):
        self.functionAccess()
        self.fillForm("aaa", "0123456789", "123a.com", "aaa")
        for x in range(1,100):
            time.sleep(0.1)
            message = self.driver.find_elements(By.ID, "validateFortxtSenderEmail")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False) 

    def test_no_input_email(self):
        self.functionAccess()
        self.fillForm("aaa", "0123456789", "", "aaa")
        for x in range(1,100):
            time.sleep(0.1)
            message = self.driver.find_elements(By.ID, "validateFortxtSenderEmail")
            if x == 99:
                if len(message)!=0: 
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)

    def test_input_message(self):
        self.functionAccess()
        self.fillForm("aa", "0123456789", "aaa@gmail.com", "aaa")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)

    def test_no_input_message(self):
        self.functionAccess()
        self.fillForm("aa", "0123456789", "aaa@gmail.com", "aaa")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "sending_code")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Thành công")
            except:
                continue
        self.assertTrue(check)

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
