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
        self.driver.get("https://batdongsan.com.vn/ho-tro-tien-ich/ht-xem-tuoi-xay-nha")

    def pressSubmit(self):
        buttonSubmit = self.driver.find_element(By.ID, "btnSubmitBuildAge")
        buttonSubmit.click()

    def fillForm(self, age, year):
        self.driver.find_element(By.ID, "AgeBuildBirthYear").send_keys(age)
        Select(self.driver.find_element(By.ID, "Year")).select_by_value(year)
        self.pressSubmit()

    def clearForm(self):
        self.driver.find_element(By.ID, "AgeBuildBirthYear").clear()
        Select(self.driver.find_element(By.ID, "Year")).select_by_index(0)


    def test_valid_age(self):
        self.fillForm("1960", "2030")
        try:
            divHeader = self.driver.find_element(By.CLASS_NAME, "divHeader").get_attribute("innerHTML")
            print(divHeader)
            if len(divHeader):
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_fail_age(self):
        self.fillForm("1850", "2030")
        try:
            divHeader = self.driver.find_element(By.CLASS_NAME, "divHeader").get_attribute("innerHTML")
            if len(divHeader):
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_string_in_age(self):
        self.fillForm("aaa", "2030")
        message = self.driver.find_element(By.XPATH, '//div[@class="validateMessage"]//span[@for="AgeBuildBirthYear"]')
        self.assertTrue(message.get_attribute("innerHTML") == "Năm sinh nhập vào chưa đúng")

    def test_noinput_in_age(self):
        self.fillForm("", "2030")
        message = self.driver.find_element(By.XPATH, '//div[@class="validateMessage"]//span[@for="AgeBuildBirthYear"]')
        self.assertTrue(message.get_attribute("innerHTML") == "Bạn vui lòng điền năm sinh")

    def test_dropdown_year(self):
        self.fillForm("2000", "2030")
        year = self.driver.find_element(By.XPATH, '//select[@id="Year"]//option[@selected="selected"]').get_attribute('innerHTML')
        if year == "2030":
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_age_greater_year(self):
        self.fillForm("2035", "2030")
        message = self.driver.find_element(By.XPATH, '//div[@id="divFormBuildAge"]//div[@id="validationBuildAgeMessage"]')
        self.assertTrue(message.get_attribute("innerHTML") == "Năm sinh của gia chủ phải nhỏ hơn năm dự kiến xây dựng")

    def test_year_greater_age(self):
        self.fillForm("2025", "2030")
        try:
            divHeader = self.driver.find_element(By.CLASS_NAME, "divHeader").get_attribute("innerHTML")
            if len(divHeader):
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_age_equal_year(self):
        self.fillForm("2025", "2025")
        try:
            divHeader = self.driver.find_element(By.CLASS_NAME, "divHeader").get_attribute("innerHTML")
            if len(divHeader):
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
