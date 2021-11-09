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
        self.driver.get('https://batdongsan.com.vn/nha-moi-gioi')
        time.sleep(1)
        a = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[4]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/a[1]")
        a.click()
        time.sleep(2)
        print("==========================START-TEST==========================")

                
    def test_No1(self):
        """LIÊN HỆ VỚI NHÀ MÔI GIỚI ĐỦ FIELD """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            time.sleep(10)
            check = self.driver.find_element(By.ID, "success")
            self.assertTrue(check.text == "Thông tin liên hệ của bạn đã được gửi tới nhà môi giới thành công.")
        except:
            assert False
        finally:
            assert True
    def test_No2(self):
        """THIẾU TIÊU ĐỀ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("")
        self.driver.find_element(by=By.ID, value="Name").send_keys("A")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn vui lòng điền tiêu đề")
        except:
            assert False
        finally:
            assert True
    def test_No3(self):
        """ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn vui lòng điền tên liên hệ")
        except:
            assert False
        finally:
            assert True
    def test_No4(self):
        """ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn vui lòng điền thông tin email")
        except:
            assert False
        finally:
            assert True
    def test_No5(self):
        """ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn vui lòng điền nội dung")
        except:
            assert False
        finally:
            assert True
    def test_No6(self):
        """ """    
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn vui lòng nhập mã an toàn")
        except:
            assert False
        finally:
            assert True
    def test_No7(self):
        """ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a@gmail.com")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            time.sleep(3)
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Gửi mail thất bại. Nhập sai captcha")
        except:
            assert False
        finally:
            assert True
    def test_No8(self):
        """ """
        self.driver.find_element(by=By.ID, value="Title").send_keys("a")
        self.driver.find_element(by=By.ID, value="Name").send_keys("a")
        self.driver.find_element(by=By.ID, value="FromEmail").send_keys("a")
        self.driver.find_element(by=By.ID, value="Content").send_keys("a")
        self.driver.find_element(by=By.ID, value="codeRegister").send_keys("3LJX")
        try:
            fieldValidator = self.driver.find_element(By.ID, "btnSendMail")
            fieldValidator.click()
            check = self.driver.find_element(By.CLASS_NAME, "field-validation-error")
            self.assertTrue(check.text == "Bạn nhập sai định dạng mail")
        except:
            assert False
        finally:
            assert True
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()