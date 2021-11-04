import time

import unittest
import mydata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By


class PythonSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.username = mydata.username
        self.password = mydata.password
        cService = Service(ChromeDriverManager().install())
        options = Options()
        #options.add_argument("--log-level=3")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.get("https://batdongsan.com.vn/")
        # self.driver.set_window_size(1600, 1000)
        self.driver.delete_all_cookies()

        print("==========================START-TEST==========================")

    
    def login(self):
        time.sleep(1)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        self.driver.find_element(
            by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(
            by=By.ID, value="Password").send_keys(self.password)
        self.driver.find_element(by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)
        self.driver.find_elements(By.CLASS_NAME, "user-name")[1].click()
        time.sleep(2)
        self.driver.find_element(
            By.CLASS_NAME, "menu-user-child.show").find_elements(By.TAG_NAME,"li")[1].click()
        time.sleep(5)
    
    def test_01(self):
        self.login()
        self.find_element(By.ID, "txtFullname").clear()
        self.find_element(By.ID, "MainContent__userPage_ctl00_btnSave").click()
        error = self.find_element(
            By.ID, "errorFullName").get_atrribute('innerHTML')
        self.assertTrue(error == "Bạn cần nhập thông tin")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

