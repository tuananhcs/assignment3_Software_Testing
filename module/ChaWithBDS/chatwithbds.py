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


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get('https://batdongsan.com.vn/')
        time.sleep(10)
        a = self.driver.find_element(By.CLASS_NAME, "lc-9blymn e16i86ec0")
        print(a.text)
        time.sleep(5)
        print("==========================START-TEST==========================")

    def test_No1(self):
        """Search without a character and don't select "Loại nhà đất" """

    
        self.driver.find_element(by=By.ID, value="name").send_keys("a")
        self.driver.find_element(by=By.ID, value="email").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="ff6rxawai3_3").send_keys("a")
        self.driver.find_element(by=By.ID, value="ff6rxawai3_3").send_keys("a")
        check = False
        for _ in range(1,50):
            try:
                time.sleep(0.1)
                fancyBox = self.driver.find_element(By.CLASS_NAME, "Linkify")
                if fancyBox: 
                    check = (fancyBox.get_attribute("innerHTML") == "Cảm ơn Anh/Chị! Lời nhắn đã được gửi đi. Nhóm hỗ trợ  sẽ sớm liên hệ với Anh/Chị.")
                    x = 50
            except:
                continue
        self.assertTrue(check)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()