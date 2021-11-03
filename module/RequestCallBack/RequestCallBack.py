from re import match
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
        # PATH = "C:\Program Files (x86)\chromedriver.exe"
        # self.driver = webdriver.Chrome(PATH)
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.set_page_load_timeout(10)
        # self.driver.set_script_timeout(10)
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get("https://batdongsan.com.vn/nha-dat-ban")

    def pressSubmit(self):
        buttonSubmit = self.driver.find_element(By.LINK_TEXT, "Gửi yêu cầu")
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

    def isValidPhone(self, s):
        reg = re.compile("^(0|\\+84)(\\s|\\.)?((3[2-9])|(5[689])|(7[06-9])|(8[1-689])|(9[0-46-9]))(\\d)(\\s|\\.)?(\\d{3})(\\s|\\.)?(\\d{3})$")
        return reg.match(s)

    def isValidEmail(self, s):
        regex = re.compile("^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$")
        return regex.match(s)

    def checkFill(self, field, value):
        try:
            fill = self.driver.find_element(By.NAME, field)
            fill.send_keys(value)
            fill.send_keys(Keys.ENTER)

            self.pressSubmit()
            
            fieldValidator = self.driver.find_element(By.CLASS_NAME, "error-message".format(field))

            if value == "":
                print(fieldValidator.get_attribute("innerHTML"))
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Vui lòng nhập số điện thoại hoặc email.")
            elif field == "txtSenderMobile" and self.isValid(value) == False:
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Số điện thoại nhập vào không đúng.")
            elif field == "txtSenderEmail" and self.isValidEmail(value) == False:
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Email không hợp lệ")
        except:
            if (field == "txtSenderMobile" and self.isValid(value) == True) or (field == "txtSenderEmail" and self.isValidEmail(value) == True):
                self.assertTrue(True)
            else:
                self.assertTrue(False)

    def functionAccess(self):
        first = self.driver.find_element(By.XPATH, "//div[@id='product-lists-web']//a[@class='js__product-link-for-product-id']")
        first.click()
        btnCallBack = self.driver.find_element(By.LINK_TEXT, "Yêu cầu liên hệ lại")
        btnCallBack.click()
        time.sleep(5)



    def test_RS1(self):
        self.functionAccess()
        self.fillForm("aa", "0123456789", "ádd", "aaa")

        # result1 = self.driver.find_element(By.XPATH, './/div[@class="utils-result"]')
        # h1 = result1.get_attribute('innerHTML')
        # self.clearForm()
        # self.fillForm(10, 10, 2, 2, 1)
        # result2 = self.driver.find_element(By.XPATH, './/div[@class="utils-result"]')
        # h2 = result2.get_attribute('innerHTML')
        # self.assertTrue(h1 == h2)

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
