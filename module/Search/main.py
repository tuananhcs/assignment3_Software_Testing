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
        self.driver = webdriver.Chrome(options=options, service=cService)
        self.driver.get("https://batdongsan.com.vn/")
        # self.driver.set_window_size(1600, 1000)
        self.driver.delete_all_cookies()

        print("==========================START-TEST==========================")

    def clickSearchButton(self):
        self.driver.find_element(By.ID, "btnSearch").click()

    def clickSearchBar(self):
        self.driver.find_element(By.ID, "txtSearch").click()

    def select_city(self):
        time.sleep(2)
        self.driver.find_elements(
            By.CLASS_NAME, "select-text.select-custom")[1].click()
        time.sleep(2)
        self.driver.find_element(By.ID, "divCityOptions").find_element(
            By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()

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

    # def test_NoDS1(self):
    #     """Search without a character and don't select "Loại nhà đất" """
    #     self.clickSearchBar()
    #     self.clickSearchButton()

    # def test_NoDS2(self):
    #     """Search without a character and  select "Loại nhà đất" """
    #     time.sleep(5)
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "re__select__selected-value.select-text.select-custom")[0].click()
    #     self.driver.find_element(By.ID, "divCatagoryReOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     self.clickSearchButton()

    # def test_NoSN01(self):
    #     """Search without a character and  select "Bất động sản gần bạn " """
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     time.sleep(3)
    #     self.driver.find_element(By.CLASS_NAME, "ui-menu-item").find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").click()
    #     self.clickSearchButton()

    # def test_SA001(self):
    #     """Search without a character and  select data in "Trên toàn quốc" dropdown button"""
    #     self.select_city_distric()
    #     time.sleep(2)
    #     self.clickSearchButton()

    # def test_NMG001(self):
    #     """Chưa dc Search without a character and  select "Mức giá" by scrollbar"""
    #     time.sleep(2)
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "select-text.select-custom")[2].click()
    #     time.sleep(3)
    #     # print(self.driver.find_element(By.ID, "divPriceOptions").find_element(
    #     #     By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].get_attribute("innerHTML"))
    #     self.driver.find_element(By.ID, "divPriceOptions").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     self.clickSearchButton()
    #     #time.sleep(2)

    # def test_NDT001(self):
    #     """Search without a character and  select "Diện tích" by dropdown button"""
    #     time.sleep(2)
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "select-text.select-custom")[3].click()
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "divAreaOptions").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[3].click()
    #     time.sleep(2)
    #     self.clickSearchButton()

    # def test_NDT002(self):
    #     """Search without a character and  select "Diện tích" by dropdown button"""
    #     time.sleep(2)
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "select-text.select-custom")[3].click()
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "txtAreaMinValue").send_keys("100")
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "txtAreaMaxValue").send_keys("200")
    #     time.sleep(2)
    #     self.clickSearchButton()
    #     #time.sleep(2)

    # def test_NDT003(self):
    #     """Search without a character and  select "Diện tích" by dropdown button"""
    #     time.sleep(2)
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "select-text.select-custom")[3].click()
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "divAreaOptions").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     time.sleep(2)
    #     self.clickSearchButton()

    # def test_NDA001(self):
    #     """ Search without a character and  select Dự án """
    #     self.select_city()
    #     time.sleep(0.5)
    #     #select Dự án
    #     self.driver.find_elements(
    #         By.CLASS_NAME, "select-text.select-custom")[4].click()
    #     # print(self.driver.find_element(By.ID, "divProjectOptions").find_element(
    #     #     By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].get_attribute("innerHTML"))
    #     self.driver.find_element(By.ID, "divProjectOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].click()
    #     time.sleep(0.5)
    #     self.clickSearchButton()
    #     #time.sleep(0.5)

    # def test_NPX001(self):
    #     """ Search without a character and  select "Phường xã" """
    #     self.select_city_distric()
    #     time.sleep(1.5)
    #     self.driver.find_element(
    #         By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
    #     time.sleep(0.5)
    #     #click Phuong, xa button
    #     self.driver.find_element(By.ID, "divWard").find_element(
    #         By.TAG_NAME, "span").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "divWardOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     time.sleep(0.5)
    #     self.clickSearchButton()

    # def test_NDP001(self):
    #     """ Search without a character and  select "Đường phố" """
    #     self.select_city_distric_town()
    #     time.sleep(0.5)
    #     self.driver.find_element(
    #         By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
    #     time.sleep(0.5)
    #     #click Duong pho button
    #     self.driver.find_element(By.ID, "divStreet").find_element(
    #         By.TAG_NAME, "span").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "divStreetOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     time.sleep(0.5)
    #     self.clickSearchButton()

    # def test_NHNP001(self):
    #     """ Search without a character and  select "Hướng nhà" """
    #     time.sleep(3)
    #     self.driver.find_element(By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
    #     time.sleep(2)
    #     #click so phong
    #     self.driver.find_element(By.ID, "divBedRoom").find_element(
    #         By.TAG_NAME, "span").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "divBedRoomOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[2].click()
    #     time.sleep(0.5)
    #     self.clickSearchButton()

    # def test_NHNP002(self):
    #     """ Search without a character and  select "Hướng nhà" """
    #     time.sleep(3)
    #     self.driver.find_element(
    #         By.CLASS_NAME, "re__btn.re__btn-pr-ghost-inverted--sm.re__btn-icon-right--sm.filter-more").click()
    #     time.sleep(2)
    #     #click so phong
    #     self.driver.find_element(By.ID, "divBedRoom").find_element(
    #         By.TAG_NAME, "span").click()
    #     time.sleep(0.5)
    #     self.driver.find_element(By.ID, "divBedRoomOptions").find_element(
    #         By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")[1].click()
    #     time.sleep(0.5)
    #     self.clickSearchButton()

    # def test_S1C(self): 
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(By.ID, "txtSearch").send_keys(self.character)
    #     self.clickSearchButton()
    #     #time.sleep(5)

    # def test_SOneorMoreSpace(self):
    #     """Search with text have only one or more space character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(By.ID, "txtSearch").send_keys(self.twospace)
    #     time.sleep(5)
    #     self.clickSearchButton()
    #     #time.sleep(5)
    
    # def test_SNoSpace(self):
    #     """Search a string and no space character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.string_no_space)
    #     time.sleep(5)
    #     self.clickSearchButton()
    
    # def test_SSpace(self):
    #     """Search a string with space character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.text_with_space)
    #     time.sleep(5)
    #     self.clickSearchButton()
    
    # def test_SSpecial(self):
    #     """Search a string with special character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.special)
    #     time.sleep(5)
    #     self.clickSearchButton()
    
    # def test_SUnicode(self):
    #     """Search a string with unicode character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.unicodeText)
    #     time.sleep(5)
    #     self.clickSearchButton()
    #     #time.sleep(10)

    # def test_SLink(self):
    #     """Search a link"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.link)
    #     time.sleep(5)
    #     self.clickSearchButton()

    # def test_Shieroglyphics(self):
    #     """Search a string with hieroglyphics character"""
    #     time.sleep(2)
    #     self.clickSearchBar()
    #     self.driver.find_element(
    #         By.ID, "txtSearch").send_keys(self.foreignlanguage)
    #     time.sleep(5)
    #     self.clickSearchButton()
        


    



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
