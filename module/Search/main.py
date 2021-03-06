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

        self.character = mydata.character
        self.twospace = mydata.twospace
        self.string_no_space = mydata.string_no_space
        self.text_with_space = mydata.text_with_space
        self.special = mydata.special
        self.unicodeText = mydata.unicodeText
        self.link = mydata.link
        self.foreignlanguage = mydata.foreignlanguage
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
        # self.driver.set_window_size(1600, 1000)
        self.driver.delete_all_cookies()

        # print("==========================START-TEST==========================")

    def clickSearchButton(self):
        self.driver.find_element(By.ID, "btnSearch").click()

    def clickSearchBar(self):
        self.driver.find_element(By.ID, "txtSearch").click()

    def select_city(self):
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[1].click()
        time.sleep(2)
        self.driver.find_element(By.ID, "divCityOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(2)

    def select_city_distric(self):
        time.sleep(3)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[1].click()
        time.sleep(2)
        self.driver.find_element(By.ID, "divCityOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(2)
        self.driver.find_element(By.ID, "divCityOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()

    def test_NoDS1(self):
        """Search without a character and don't select "Lo???i nh?? ?????t" """
        time.sleep(3)
        self.clickSearchBar()
        time.sleep(3)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NoDS2(self):
        """Search without a character and  select "Lo???i nh?? ?????t" """
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "re__select__selected-value.select-text.select-custom")[0].click()
        self.driver.find_element(By.ID, "divCatagoryReOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NoSN01(self):
        """Search without a character and  select "B???t ?????ng s???n g???n b???n " """
        time.sleep(5)
        self.clickSearchBar()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "ui-menu-item").find_element(
            By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").click()
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NoSC01(self):
        """Search without a character and  select one of "T??m ki???m g???n ????y"  """
        time.sleep(5)
        self.clickSearchBar()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "ui-menu-item").find_element(
            By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").click()
        time.sleep(5)
        self.clickSearchButton()
        time.sleep(3)
        self.driver.find_element(
            By.CLASS_NAME, "re__left-menu").find_element(By.TAG_NAME, "h2").click()
        time.sleep(3)
        self.clickSearchBar()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "re__searching-history.ui-menu-item").find_elements(
            By.TAG_NAME, "a")[0].click()

        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_SA001(self):
        """Search without a character and  select data in "Tr??n to??n qu???c" dropdown button"""
        self.select_city_distric()
        time.sleep(2)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NMG001(self):
        """Ch??a dc Search without a character and  select "M???c gi??" by scrollbar"""
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[2].click()
        time.sleep(5)
        # print(self.driver.find_element(By.ID, "divPriceOptions").find_element(
        #     By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].get_attribute("innerHTML"))
        self.driver.find_element(By.ID, "divPriceOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(2)
        self.clickSearchButton()
        # time.sleep(2)
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NDT001(self):
        """Search without a character and  select "Di???n t??ch" by dropdown button"""
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[3].click()
        time.sleep(5)
        self.driver.find_element(By.ID, "divAreaOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[3].click()
        time.sleep(2)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NDT002(self):
        """Search without a character and  select "Di???n t??ch" by dropdown button"""
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[3].click()
        time.sleep(5)
        self.driver.find_element(By.ID, "txtAreaMinValue").send_keys("100")
        time.sleep(2)
        self.driver.find_element(By.ID, "txtAreaMaxValue").send_keys("200")
        time.sleep(2)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False
        # time.sleep(2)

    def test_NDT003(self):
        """Search without a character and  select "Di???n t??ch" by dropdown button"""
        time.sleep(5)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[3].click()
        time.sleep(5)
        self.driver.find_element(By.ID, "divAreaOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(3)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NDA001(self):
        """ Search without a character and  select D??? ??n """
        self.select_city()
        time.sleep(3)
        # select D??? ??n
        self.driver.find_element(
            By.ID, "divProject").click()
        time.sleep(3)
        # print(self.driver.find_element(By.ID, "divProjectOptions").find_element(
        #     By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].get_attribute("innerHTML"))
        self.driver.find_element(By.ID, "divProjectOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].click()
        time.sleep(3)
        self.clickSearchButton()
        # time.sleep(0.5)
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NPX001(self):
        """ Search without a character and  select "Ph?????ng x??" """
        self.select_city_distric()
        time.sleep(3)
        self.driver.find_element(
            By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
        time.sleep(3)
        # click Phuong, xa button
        self.driver.find_element(By.ID, "divWard").find_element(
            By.TAG_NAME, "span").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "divWardOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(3)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NDP001(self):
        """ Search without a character and  select "???????ng ph???" """
        self.select_city_distric()
        time.sleep(0.5)
        self.driver.find_element(
            By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
        time.sleep(0.5)
        # click Duong pho button
        self.driver.find_element(By.ID, "divStreet").find_element(
            By.TAG_NAME, "span").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "divStreetOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(0.5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NHNP001(self):
        """ Search without a character and  select "H?????ng nh??" """
        time.sleep(3)
        self.driver.find_element(
            By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "divHomeDirection").find_element(
            By.TAG_NAME, "span").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "divHomeDirectionOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NSP001(self):
        """ Search without a character and  select "S??? ph??ng"""""
        time.sleep(3)
        self.driver.find_element(
            By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
        time.sleep(2)
        # click so phong
        self.driver.find_element(By.ID, "divBedRoom").find_element(
            By.TAG_NAME, "span").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "divBedRoomOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].click()
        time.sleep(0.5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_NSP002(self):
        """ Search without a character and  select "S??? ph??ng"""""
        time.sleep(3)
        self.driver.find_element(
            By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
        time.sleep(2)
        # click so phong
        self.driver.find_element(By.ID, "divBedRoom").find_element(
            By.TAG_NAME, "span").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "divBedRoomOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(0.5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_S1C(self):
        time.sleep(2)
        self.clickSearchBar()
        self.driver.find_element(By.ID, "txtSearch").send_keys(self.character)
        self.clickSearchButton()

        # time.sleep(5)
        try: 
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except: 
            assert False

    def test_SOneorMoreSpace(self):
        """Search with text have only one or more space character"""
        # time.sleep(5)

        self.driver.find_element(By.ID, "txtSearch").send_keys(self.twospace)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False
        #time.sleep(5)
    
    def test_SNoSpace(self):
        """Search a string and no space character"""
        time.sleep(2)

        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.string_no_space)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False
        
    
    def test_SSpace(self):
        """Search a string with space character"""
        time.sleep(2)

        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.text_with_space)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False
    
    def test_SSpecial(self):
        """Search a string with special character"""
        time.sleep(2)

        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.special)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False
    
    def test_SUnicode(self):
        """Search a string with unicode character"""
        time.sleep(2)
        # time.sleep(10)
        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.unicodeText)
        time.sleep(5)
        self.clickSearchButton()
        
        #time.sleep(10)
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_SLink(self):
        """Search a link"""
        time.sleep(2)
        self.clickSearchBar()
        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.link)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False

    def test_Shieroglyphics(self):
        """Search a string with hieroglyphics character"""
        time.sleep(2)
        self.clickSearchBar()
        self.driver.find_element(
            By.ID, "txtSearch").send_keys(self.foreignlanguage)
        time.sleep(5)
        self.clickSearchButton()
        try:
            self.driver.find_element(By.CLASS_NAME, "re__srp-total-count")
            assert True
        except:
            assert False


    



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
