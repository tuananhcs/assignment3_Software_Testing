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

class DetailedEstimate(unittest.TestCase):
    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get("https://batdongsan.com.vn/ho-tro-tien-ich/ht-du-toan-chi-tiet")

    def test_CD1(self):
        # wait = WebDriverWait(self.driver, 10)
        # lengthHouse = wait.until(EC.presence_of_element_located((By.ID, 'Length')))
        lengthHouse = self.driver.find_element_by_id('Length')
        lengthHouse.send_keys("-1")
        # lengthHouse.send_keys(Keys.ENTER)
        lengthHouse.submit()

        # wait = WebDriverWait(self.driver, 10)
        # fieldValidator = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'field-validation-error')))
        fieldValidator = self.driver.find_element_by_class_name('field-validation-error')
        # elementxpath = self.driver.find_element(By.XPATH, "//span[@for='Length']")
        # validateMessage = self.driver.find_elements_by_class_name('validateMessage')
        print(len(fieldValidator))
        self.assertTrue(len(fieldValidator) == 4)



    def tearDown(self):
        self.driver.close()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
