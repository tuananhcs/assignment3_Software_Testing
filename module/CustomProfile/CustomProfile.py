from re import S
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


class CustomProfile(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.username = mydata.username
        self.password = mydata.password
        self.name = mydata.name
        self.unicodeString = mydata.unicodeString
        self.special = mydata.special
        self.iconString = mydata.iconString
        self.foreign = mydata.foreign


        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.get("https://batdongsan.com.vn/")
        #self.driver.set_window_size(1600, 1000)
        self.driver.delete_all_cookies()

    def login_and_goto_profile(self):
        time.sleep(0.5)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(0.5)
        self.driver.find_element(
            by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(
            by=By.ID, value="Password").send_keys(self.password)
        self.driver.find_element(
            by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)

        #If valid SDT:
        # self.driver.find_element(By.CLASS_NAME, "sc-hYZPRl.hWTMLh").click()
        # self.driver.find_elements(
        #     By.CLASS_NAME, "sc-aKZfe.drkqWO.sc-bUrJUP.ftSKDG")[1].click()

        #If fon't valid SDT
        self.driver.find_elements(By.CLASS_NAME, "user-name")[1].click()
        self.driver.find_element(By.CLASS_NAME, "menu-user-child.show").find_elements(
            By.TAG_NAME, "li")[1].find_element(By.TAG_NAME, "span").click()
        time.sleep(2)

    def press_save_button(self):
        self.driver.find_elements(By.CLASS_NAME, "button-blue")[1].click()

    def select_City(self):
        self.driver.find_element(By.ID, "ddlCities").find_elements(By.TAG_NAME, "option")[1].click()
    def select_Distric(self): 
        self.driver.find_element(By.ID, "ddlDistricts").find_elements(
            By.TAG_NAME, "option")[1].click()

    def select_default_field(self):
        self.select_City()
        self.select_Distric()

    # def test_0(self):
    #     """Edit the same data in any field"""
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     #self.press_save_button()
    #     time.sleep(5)

    # def test_SDT(self):
    #     """Edit the same data in any field"""
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.press_save_button()
    #     sucess_notification = self.driver.find_element(
    #         By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
    #     ############################################3
    #     self.assertTrue(sucess_notification == "Thay đổi thông tin thành công !")
    #     time.sleep(5)


    # def test_DF(self):
    #     """Don't fill in "Họ và tên" field """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(By.ID, "txtFullname").clear()
    #     self.press_save_button()
    #     error = self.driver.find_element(
    #         By.ID, "errorFullName").get_attribute('innerHTML')
    #     self.assertTrue(error == "Bạn cần nhập thông tin")
       

    

    # def test_PDF(self):
    #     """Press "Họ và tên" field but  don't fill data"""
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(By.ID, "txtFullname").click()
    #     time.sleep(2)
    #     self.press_save_button()
    #     error = self.driver.find_element(
    #         By.ID, "errorFullName").get_attribute('innerHTML')
    #     self.assertTrue(error != "Bạn cần nhập thông tin")

    # def test_FIU(self):
    #     """Fill valid "Họ và tên"  """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(By.ID, "txtFullname").clear()
    #     self.driver.find_element(By.ID, "txtFullname").send_keys(self.name)
    #     time.sleep(0.5)
    #     self.press_save_button()
    #     sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
    #     self.assertTrue(sucess_notification == "Thay đổi thông tin thành công !")

    # def test_FIUC1(self):
    #     """Fill  "Họ và tên"   with unicode"  """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(By.ID, "txtFullname").clear()
    #     self.driver.find_element(By.ID, "txtFullname").send_keys(self.unicodeString)
    #     time.sleep(0.5)
    #     self.press_save_button()
    #     sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
    #     self.assertTrue(sucess_notification == "Thay đổi thông tin thành công !")

    # def test_FIUC2(self):
    #     """Fill "Họ và tên"   with special character and number"  """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(By.ID, "txtFullname").clear()
    #     self.driver.find_element(By.ID, "txtFullname").send_keys(self.special)
    #     time.sleep(0.5)
    #     self.press_save_button()
    #     sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
    #     self.assertTrue(sucess_notification == "Thay đổi thông tin thành công !")

    # def test_FIUC3(self):
    #     """Fill  "Họ và tên"   with icon"  """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(
    #         By.ID, "txtFullname").clear()
    #     self.driver.find_element(By.ID, "txtFullname").send_keys(self.iconString)
    #     time.sleep(0.5)
    #     self.press_save_button()
    #     error = self.driver.find_element(By.ID, "errorFullName").get_attribute('innerHTML')
    #     print(error)
    #     self.assertTrue(error == "Bạn cần nhập thông tin")

    # def test_FFLN(self):
    #     """Fill  "Họ và tên" with hieroglyphics character  """
    #     self.login_and_goto_profile()
    #     self.select_default_field()
    #     self.driver.find_element(
    #         By.ID, "txtFullname").clear()
    #     self.driver.find_element(
    #         By.ID, "txtFullname").send_keys(self.foreign)
    #     time.sleep(0.5)
    #     self.press_save_button()
    #     error = self.driver.find_element(
    #         By.ID, "errorFullName").get_attribute('innerHTML')
    #     self.assertTrue(error == "Bạn cần nhập lại \"Họ tên\" cho đúng")



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

