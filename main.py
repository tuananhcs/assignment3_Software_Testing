import time
import os
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumDriver(object):
    def __init__(
        self,
        # chromedriver path
        driver_path='./chrome_driver/chromedriver_win32/chromedriver.exe',
        # pickle file path to store cookies
        cookies_file_path='./Cookies',
        # list of websites to reuse cookies with
        cookies_websites=["https://tinhte.vn"]

    ):
        self.driver_path = driver_path
        self.cookies_file_path = cookies_file_path
        self.cookies_websites = cookies_websites
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path,
            options=chrome_options
        )
        try:
            # load cookies for given websites
            cookies = pickle.load(open(self.cookies_file_path, "rb"))
            for website in self.cookies_websites:
                self.driver.get(website)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
        except Exception as e:
            # it'll fail
            # for the first time, when cookie file is not present
            print(str(e))
            print("Error loading cookies")

    def save_cookies(self):
        # save cookies
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookies_file_path, "wb"))

    def close_all(self):
        # close all open tabs
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()


def tinhte_login(driver):
    # driver.get("https://tinhte.vn")
    # if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
    #     return True
    driver.find_element_by_partial_link_text("Đăng nhập").click()
    driver.find_elements_by_name("login")[2].send_keys("Ultranonexist")
    driver.find_elements_by_name("password")[2].send_keys("うずまきナルト")
    driver.find_elements_by_class_name("button.primary")[3].click()


class TinhTeAutomationTesting(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=options, service=cService)
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://tinhte.vn")

        print("==========================START-TEST==========================")

    def login_(self):
        # self.driver.close()
        # seleniumObj = SeleniumDriver(driver_path=self.PATH)
        # self.driver = seleniumObj.driver
        # if tinhte_login(self.driver):
        #     print("Already logged in")
        # else:
        #     print("Not logged in. Login")
        #     seleniumObj.save_cookies()
        tinhte_login(self.driver)

    def search_(self, str):
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name(
            "search-textbox")
        searchTextBox.send_keys(str)
        searchTextBox.send_keys(Keys.RETURN)
        # time.sleep(10)

    

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
