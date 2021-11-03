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
        # PATH = "C:\Program Files (x86)\chromedriver.exe"
        # self.driver = webdriver.Chrome(PATH)
        # PROXY = "183.91.3.146:53281"

        cService = Service(ChromeDriverManager().install())
        options = Options()
        # options.add_argument('--proxy-server=%s' % PROXY)
        options.add_argument("--log-level=3")
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.delete_all_cookies()
        # self.driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":True})
        # self.driver.set_page_load_timeout(10)
        # self.driver.set_script_timeout(10)
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get("https://batdongsan.com.vn/ho-tro-tien-ich/ht-du-toan-chi-tiet")

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
    
    def test_CD1(self):
        houseLength = -1
        self.fillForm(houseLength, 10, 2, 2, 1)
        self.checkAlert("Length", houseLength)
    
    def test_CD2(self):
        houseLength = 10
        self.fillForm(houseLength, 10, 2, 2, 1)
        self.checkAlert("Length", houseLength)

    def test_CD3(self):
        houseLength = 51
        self.fillForm(houseLength, 10, 2, 2, 1)
        self.checkAlert("Length", houseLength)

    def test_CD4(self):
        houseLength = "a"
        self.fillForm(houseLength, 10, 2, 2, 1)
        self.checkAlert("Length", houseLength)

    def test_CD5(self):
        houseLength = ""
        self.fillForm(houseLength, 10, 2, 2, 1)
        self.checkAlert("Length", houseLength)

    def test_CR1(self):
        houseWidth = -1
        self.fillForm(10, houseWidth, 2, 2, 1)
        self.checkAlert("Width", houseWidth)
    
    def test_CR2(self):
        houseWidth = 10
        self.fillForm(10, houseWidth, 2, 2, 1)
        self.checkAlert("Width", houseWidth)

    def test_CR3(self):
        houseWidth = 51
        self.fillForm(10, houseWidth, 2, 2, 1)
        self.checkAlert("Width", houseWidth)

    def test_CR4(self):
        houseWidth = "a"
        self.fillForm(10, houseWidth, 2, 2, 1)
        self.checkAlert("Width", houseWidth)

    def test_CR5(self):
        houseWidth = ""
        self.fillForm(10, houseWidth, 2, 2, 1)
        self.checkAlert("Width", houseWidth)

    def test_STC1(self):
        houseStageNumber = -1
        self.fillForm(10, 10, houseStageNumber, 2, 1)
        self.checkAlert("StageNumber", houseStageNumber)
    
    def test_STC2(self):
        houseStageNumber = 10
        self.fillForm(10, 10, houseStageNumber, 2, 1)
        self.checkAlert("StageNumber", houseStageNumber)

    def test_STC3(self):
        houseStageNumber = 25
        self.fillForm(10, 10, houseStageNumber, 2, 1)
        self.checkAlert("StageNumber", houseStageNumber)

    def test_STC4(self):
        houseStageNumber = "a"
        self.fillForm(10, 10, houseStageNumber, 2, 1)
        self.checkAlert("StageNumber", houseStageNumber)

    def test_STC5(self):
        houseStageNumber = ""
        self.fillForm(10, 10, houseStageNumber, 2, 1)
        self.checkAlert("StageNumber", houseStageNumber)

    def test_CCMT1(self):
        houseStageHeight = -1
        self.fillForm(10, 10, 2, houseStageHeight, 1)
        self.checkAlert("StageHeight", houseStageHeight)
    
    def test_CCMT2(self):
        houseStageHeight = 4
        self.fillForm(10, 10, 2, houseStageHeight, 1)
        self.checkAlert("StageHeight", houseStageHeight)

    def test_CCMT3(self):
        houseStageHeight = 10
        self.fillForm(10, 10, 2, houseStageHeight, 1)
        self.checkAlert("StageHeight", houseStageHeight)

    def test_CCMT4(self):
        houseStageHeight = "a"
        self.fillForm(10, 10, 2, houseStageHeight, 1)
        self.checkAlert("StageHeight", houseStageHeight)

    def test_CCMT5(self):
        houseStageHeight = ""
        self.fillForm(10, 10, 2, houseStageHeight, 1)
        self.checkAlert("StageHeight", houseStageHeight)

    def test_LMN1(self):
        rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
        self.pressSubmit()
    
    def test_LMN2(self):
        rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
        rooftype.click()
        Select(rooftype).select_by_value(rooftype.get_attribute("value"))
        self.pressSubmit()

    def test_LMN3(self):
        rooftype = self.driver.find_element(By.XPATH, './/select[@id="RoofType"]')
        rooftype.click()
        Select(rooftype).select_by_value("3")
        self.pressSubmit()

    def test_RS1(self):
        self.fillForm(10, 10, 2, 2, 1)
        result1 = self.driver.find_element(By.ID, 'tabResult4')
        h1 = result1.get_attribute('innerHTML')
        self.clearForm()
        self.fillForm(10, 10, 2, 2, 1)
        result2 = self.driver.find_element(By.ID, 'tabResult4')
        h2 = result2.get_attribute('innerHTML')
        self.assertTrue(h1 == h2)

    def test_RS2(self):
        self.fillForm(10, 10, 2, 2, 1)
        result1 = self.driver.find_element(By.ID, 'tabResult4')
        h1 = result1.get_attribute('innerHTML')
        # self.driver.get(self.driver.current_url)
        time.sleep(3)
        self.pressSubmit()
        i = 3
        alert_displayed = False
        while i > 0:
            time.sleep(1)
            self.driver.refresh()
            # self.driver.find_element(By.NAME, "s").send_keys(Keys.F5)
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                alert_displayed = True
            except:
                i = i - 1
        if alert_displayed == False:
            print("Alert not show")
            self.assertTrue(False)
        alert = self.driver.switch_to.alert
        if alert.is_displayed():
            alert.accept()
        else:
            self.assertTrue(False)
            self.driver.switch_to
        self.driver.switch_to.window(self.driver.window_handles[0])
        result2 = self.driver.find_element(By.ID, 'tabResult4')
        h2 = result2.get_attribute('innerHTML')
        self.assertTrue(h1 == h2)

    def test_RS3(self):
        self.fillForm(10, 10, 2, 2, 1)
        result1 = self.driver.find_element(By.ID, 'tabResult4')
        h1 = result1.get_attribute('innerHTML')
        self.clearForm()
        self.fillForm(10, 10, 2, 2, 1)
        result2 = self.driver.find_element(By.ID, 'tabResult4')
        h2 = result2.get_attribute('innerHTML')
        self.assertTrue(h1 == h2)

    def test_UN1(self):
        self.fillForm(10, 10, 2, 2, 1)
        self.driver.find_element(By.ID, 'tabResult4')
        child_results = self.driver.find_elements(By.CLASS_NAME, 'result_chiphi_item')

        check = True

        check = check and self.checkUnit(child_results[0].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[1].find_element(By.XPATH, './/div[@class="column3"]/div'), "viên")
        check = check and self.checkUnit(child_results[2].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[3].find_element(By.XPATH, './/div[@class="column3"]/div'), "m3")
        check = check and self.checkUnit(child_results[4].find_element(By.XPATH, './/div[@class="column3"]/div'), "m3")
        check = check and self.checkUnit(child_results[5].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[6].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[7].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[8].find_element(By.XPATH, './/div[@class="column3"]/div'), "kg")
        check = check and self.checkUnit(child_results[9].find_element(By.XPATH, './/div[@class="column3"]/div'), "m2")

        self.assertTrue(check)

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
