import time
import os
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
        self.driver.get("https://m.batdongsan.com.vn/ho-tro-tien-ich/ht-du-toan-chi-tiet")

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

    def clearForm(self):
        self.driver.find_element(By.ID, "Length").clear()
        self.driver.find_element(By.ID, "Width").clear()
        self.driver.find_element(By.ID, "StageNumber").clear()
        self.driver.find_element(By.ID, "StageHeight").clear()
        Select(self.driver.find_element(By.ID, "RoofType")).select_by_index(0)

    def inputTextbox(self, field, value):
        try:
            # wait = WebDriverWait(self.driver, 3)
            lengthHouse = self.driver.find_element(By.ID, field)
            lengthHouse.send_keys(value)
            lengthHouse.send_keys(Keys.ENTER)
            # time.sleep(3)
            
            self.pressSubmit()

            # fieldValidator = self.driver.find_elements_by_class_name('field-validation-error')
            # fieldValidator = wait.until(EC.visibility_of_element_located((By.XPATH, './/span[@for="{}"]'.format(field))))
            fieldValidator = self.driver.find_element(By.XPATH, './/span[@for="{}"]'.format(field))
            
            if value == "":
                print(fieldValidator.get_attribute("innerHTML"))
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
        except:
            if type(value) is int and value in range(1, 51):
                self.assertTrue(True)
            else:
                self.assertTrue(False)
    
    # def test_CD1(self):
    #     self.inputTextbox("Length", -1)
    
    # def test_CD2(self):
    #     self.inputTextbox("Length", 10)

    # def test_CD3(self):
    #     self.inputTextbox("Length", 51)

    # def test_CD4(self):
    #     self.inputTextbox("Length", "a")

    # def test_CD5(self):
    #     self.inputTextbox("Length", "")

    # def test_CR1(self):
    #     self.inputTextbox("Width", -1)
    
    # def test_CR2(self):
    #     self.inputTextbox("Width", 10)

    # def test_CR3(self):
    #     self.inputTextbox("Width", 51)

    # def test_CR4(self):
    #     self.inputTextbox("Width", "a")

    # def test_CR5(self):
    #     self.inputTextbox("Width", "")

    # def test_STC1(self):
    #     self.inputTextbox("StageNumber", -1)
    
    # def test_STC2(self):
    #     self.inputTextbox("StageNumber", 10)

    # def test_STC3(self):
    #     self.inputTextbox("StageNumber", 25)

    # def test_STC4(self):
    #     self.inputTextbox("StageNumber", "a")

    # def test_STC5(self):
    #     self.inputTextbox("StageNumber", "")

    # def test_CCMT1(self):
    #     self.inputTextbox("StageHeight", -1)
    
    # def test_CCMT2(self):
    #     self.inputTextbox("StageHeight", 4)

    # def test_CCMT3(self):
    #     self.inputTextbox("StageHeight", 10)

    # def test_CCMT4(self):
    #     self.inputTextbox("StageHeight", "a")

    # def test_CCMT5(self):
    #     self.inputTextbox("StageHeight", "")

    # def test_LMN1(self):
    #     rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
    #     self.pressSubmit()
    
    # def test_LMN2(self):
    #     rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
    #     rooftype.click()
    #     Select(rooftype).select_by_value(rooftype.get_attribute("value"))
    #     self.pressSubmit()

    # def test_LMN3(self):
    #     rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
    #     rooftype.click()
    #     Select(rooftype).select_by_value("3")
    #     self.pressSubmit()

    def test_RS1(self):
        self.fillForm(10, 10, 2, 2, 1)
        result1 = self.driver.find_element(By.XPATH, './/div[@class="utils-result"]')
        h1 = result1.get_attribute('innerHTML')
        self.clearForm()
        self.fillForm(10, 10, 2, 2, 1)
        result2 = self.driver.find_element(By.XPATH, './/div[@class="utils-result"]')
        h2 = result2.get_attribute('innerHTML')
        self.assertTrue(h1 == h2)

    def tearDown(self):
        self.driver.close()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
