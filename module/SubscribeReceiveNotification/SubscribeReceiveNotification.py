import time
import os
import unittest
from unittest import result
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DetailedEstimate(unittest.TestCase):
    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.implicitly_wait(3)
        self.driver.get("https://batdongsan.com.vn/can-mua-can-thue")

        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")

    def functionAccess(self):
        first = self.driver.find_element(By.XPATH, '//div[@class="Main"]/div[2]/div[@class="p-title"]/a')
        print(first.get_attribute("innerHTML"))
        first.click()
        emailregister = self.driver.find_element(By.ID, 'emailregister')
        emailregister.click()
        # btnCallBack = self.driver.find_element(By.LINK_TEXT, "Yêu cầu liên hệ lại")
        # btnCallBack.click()
        time.sleep(50)

    def pressSubmit(self):
        buttonSubmit = self.driver.find_element(By.XPATH, './/input[@type="submit"]')
        buttonSubmit.click()

    def fillForm(self, length, width, stageNumber, stageHeight, roofType):
        self.driver.find_element(By.ID, "Length").send_keys(length)
        self.driver.find_element(By.ID, "Width").send_keys(width)
        self.driver.find_element(By.ID, "StageNumber").send_keys(stageNumber)
        self.driver.find_element(By.ID, "StageHeight").send_keys(stageHeight)
        self.driver.find_element(By.ID, "RoofType").send_keys(roofType)
        self.pressSubmit()
        # time.sleep(30)

    def clearForm(self):
        self.driver.find_element(By.ID, "Length").clear()
        self.driver.find_element(By.ID, "Width").clear()
        self.driver.find_element(By.ID, "StageNumber").clear()
        self.driver.find_element(By.ID, "StageHeight").clear()
        Select(self.driver.find_element(By.ID, "RoofType")).select_by_index(0)

    def checkAlert(self, field, value):
        fieldValidator = None
        try:
            fieldValidator = self.driver.find_element(By.XPATH, './/span[@for="{}"]'.format(field))
        except:
            try:
                fieldValidator = self.driver.find_element(By.XPATH, './/span[@data-valmsg-for="{}"]'.format(field))
            except:
                self.assertTrue(False)
            
        if value == "":
            self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Bạn vui lòng điền giá trị")
        elif type(value) is not int or value not in range(1,51):
            if field == "Length":
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Giá trị nhập vào chưa đúng.<br>Chiều dài phải từ 1m - 50m")
            elif field == "Width":
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Giá trị nhập vào chưa đúng.<br>Chiều rộng phải từ 1m - 50m")
            elif field == "StageNumber":
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Giá trị nhập vào chưa đúng.<br>Số tầng phải từ 1 đến 20")
            elif field == "StageHeight":
                self.assertTrue(fieldValidator.get_attribute("innerHTML") == "Giá trị nhập vào chưa đúng.<br>Chiều cao phải từ 2m đến 6m")
        else:
            if fieldValidator.get_attribute("innerHTML") == "":
                try:
                    self.driver.find_element(By.ID, 'tabResult4')
                    self.assertTrue(True)
                except:
                    self.assertTrue(False)
            else: 
                self.assertTrue(False)

    def checkUnit(self, field, expect):
        if field.get_attribute("innerHTML") == expect:
            return True
        else:
            return False
    
    def test_1(self):
        self.functionAccess()

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
