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
        self.manualname = mydata.manualname
        self.taxcode = mydata.taxcode
        self.phone = mydata.phone
        self.notregisterphone = mydata.notregisterphone
        self.address = mydata.adress


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
        time.sleep(1)
        self.driver.find_element(by=By.ID, value="kct_login").click()
        time.sleep(1)
        self.driver.find_element(
            by=By.ID, value="UserName").send_keys(self.username)
        self.driver.find_element(
            by=By.ID, value="Password").send_keys(self.password)
        self.driver.find_element(
            by=By.CLASS_NAME, value="js__btn-login.re__btn.re__btn-pr-solid--md").click()
        time.sleep(5)
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
    
    def default_name(self): 
        self.driver.find_element(
            By.ID, "txtFullname").clear()
        self.driver.find_element(
            By.ID, "txtFullname").send_keys(self.name)
        self.driver.find_element(By.ID, "txtAddress").clear()
        time.sleep(2)

    def clearData(self): 
        self.driver.find_element(By.ID, "ddlWards").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.driver.find_element(By.ID, "ddlStreets").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.driver.find_element(By.ID, "txtManualName").clear()
        self.driver.find_element(By.ID, "txtSkypeIM").clear()
        self.driver.find_element(By.ID, "txtZalo").clear()
        self.driver.find_element(By.ID, "txtViber").clear()
        self.driver.find_element(By.ID, "txtTaxCode").clear()
        self.driver.find_element(By.ID, "MainContent__userPage_ctl00_rdMale").click()
     
    
    def select_default_field(self):
        self.select_City()
        self.select_Distric()

    
    def reset_avt(self): 
        self.driver.find_element(By.CLASS_NAME, "imgdelold").click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.press_save_button()
        time.sleep(3)

    def test_RLP(self):
        """002"""
        self.login_and_goto_profile()
        self.default_name()
        self.select_default_field()
        self.driver.refresh()
        assert True

    def test_EDP(self): 
        """003"""
        self.login_and_goto_profile()
        assert True

    def test_TOB(self):
        """005"""
        assert True

    def test_SDT(self):
        """004 Edit the same data in any field"""
        self.login_and_goto_profile()
        self.select_default_field()
        self.press_save_button()
        sucess_notification = self.driver.find_element(
            By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        ############################################3
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")
        time.sleep(5)


    def test_DF(self):
        """006 Don't fill in "H??? v?? t??n" field """
        self.login_and_goto_profile()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtFullname").clear()
        self.press_save_button()
        error = self.driver.find_element(
            By.ID, "errorFullName").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n nh???p th??ng tin")
       

    

    def test_PDF(self):
        """007 Press "H??? v?? t??n" field but  don't fill data"""
        self.login_and_goto_profile()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtFullname").click()
        time.sleep(2)
        self.press_save_button()
        error = self.driver.find_element(
            By.ID, "errorFullName").get_attribute('innerHTML')
        self.assertTrue(error != "B???n c???n nh???p th??ng tin")

    def test_FIU(self):
        """008 Fill valid "H??? v?? t??n"  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtFullname").clear()
        self.driver.find_element(By.ID, "txtFullname").send_keys(self.name)
        time.sleep(0.5)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FIUC1(self):
        """009 Fill  "H??? v?? t??n"   with unicode"  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtFullname").clear()
        self.driver.find_element(By.ID, "txtFullname").send_keys(self.unicodeString)
        time.sleep(0.5)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FIUC2(self):
        """010 Fill "H??? v?? t??n"   with special character and number"  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtFullname").clear()
        self.driver.find_element(By.ID, "txtFullname").send_keys(self.special)
        time.sleep(0.5)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FIUC3(self):
        """011 Fill  "H??? v?? t??n"   with icon"  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.driver.find_element(
            By.ID, "txtFullname").clear()
        self.driver.find_element(By.ID, "txtFullname").send_keys(self.iconString)
        time.sleep(0.5)
        self.press_save_button()
        error = self.driver.find_element(By.ID, "errorFullName").get_attribute('innerHTML')
        print(error)
        self.assertTrue(error == "B???n c???n nh???p th??ng tin")

    def test_FFLN(self):
        """012 Fill  "H??? v?? t??n" with hieroglyphics character  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.driver.find_element(
            By.ID, "txtFullname").clear()
        self.driver.find_element(
            By.ID, "txtFullname").send_keys(self.foreign)
        time.sleep(0.5)
        self.press_save_button()
        error = self.driver.find_element(
            By.ID, "errorFullName").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n nh???p l???i \"H??? t??n\" cho ????ng")

    def test_CS(self):
        """013 - change sex"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.driver.find_element(
            By.ID, "MainContent__userPage_ctl00_rdFemale").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
  

    def test_CA(self):
        """014 - Change avatar"""
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.reset_avt()
        self.driver.find_element(By.CLASS_NAME, "spanButtonPlaceholder").find_element(
            By.TAG_NAME, "input").send_keys("E:\HK211\TMDT\\room\BedRoom\\bed2.jpg")
        time.sleep(7)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_CARIT(self):
        """015"""
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.reset_avt()
        self.driver.find_element(By.CLASS_NAME, "spanButtonPlaceholder").find_element(
            By.TAG_NAME, "input").send_keys("E:\ST_Project_3.pdf")
        try: 
            self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span")
            assert False
        except: 
            assert True

    def test_DFTTG1(self):
        """016 Don't fill in "T??n th?????ng g???i" field   """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DFTTG2(self):
        """017 - Press "T??n th?????ng g???i" field but  don't fill data  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(By.ID, "txtManualName").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
       
    def test_FIUTTG(self):
        """018 - Fill valid "T??n th?????ng g???i"   """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtManualName").send_keys(self.manualname)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DSNS(self):
        """019 - Don't select "Ng??y sinh"   """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
     
    def test_SNS(self):
        """020 - Select "Ng??y sinh"   """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "MainContent__userPage_ctl00_txtBirthDates").click()
        #print(self.driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "a"))
        self.driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "a").click()
        time.sleep(3)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_NSTTP(self):
        """021 - No select data in "T???nh, Th??nh ph??? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.driver.find_element(By.ID, "ddlCities").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.driver.find_element(By.ID, "ddlDistricts").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.default_name()
        self.press_save_button()
        error = self.driver.find_element(By.ID, "errorCity").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n ch???n th??ng tin")

    def test_STTP(self):
        """022 - Select data in "T???nh, Th??nh ph??? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.driver.find_element(By.ID, "ddlCities").find_elements(
            By.TAG_NAME, "option")[2].click()
        self.select_Distric()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
    def test_NSQH(self):
        """023 - No select data in "Qu???n, huy???n " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.driver.find_element(By.ID, "ddlCities").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.driver.find_element(By.ID, "ddlDistricts").find_elements(
            By.TAG_NAME, "option")[0].click()
        self.default_name()
        self.press_save_button()
        error = self.driver.find_element(
            By.ID, "errorCity").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n ch???n th??ng tin")

    def test_SQH(self):
        """024 - Select data in "Qu???n, huy???n " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.select_City()
        self.driver.find_element(By.ID, "ddlDistricts").find_elements(
            By.TAG_NAME, "option")[2].click()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification=="Thay ?????i th??ng tin th??nh c??ng !")

    def test_NSPX(self):
        """025 - No select data in "Ph?????ng, x?? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_SPX(self):
        """026 - Select data in "Ph?????ng, x?? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()

        self.driver.find_element(By.ID, "ddlWards").find_elements(
            By.TAG_NAME, "option")[1].click()

        
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification=="Thay ?????i th??ng tin th??nh c??ng !")

    def test_NSDP(self):
        """027 - No select data in "???????ng, ph??? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_SDP(self):
        """028 - Select data in "???????ng, ph??? " field"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.driver.find_element(By.ID, "ddlStreets").find_elements(
            By.TAG_NAME, "option")[1].click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification=="Thay ?????i th??ng tin th??nh c??ng !")

    def test_SDDC(self):
        """029 - Select default "?????a ch???" """
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification =="Thay ?????i th??ng tin th??nh c??ng !")

    def test_FDC(self):
        """030 - Fill in "?????a ch???" field"""
        self.login_and_goto_profile()
        self.clearData()
        self.default_name()
        self.select_default_field()
        self.driver.find_element(By.ID, "txtAddress").send_keys(self.address)

        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DFCMND(self):
        """031- Don't fill in "M?? s??? thu???/CMND" field    """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DFFCMND(self):
        """032 -Press "M?? s??? thu???/CMND" field but  don't fill data  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(By.ID, "txtTaxCode").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FIUCMND(self):
        """033 - Fill valid "M?? s??? thu???/CMND"     """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtTaxCode").send_keys(self.taxcode)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification == "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DFSIM(self):
        """034 - Don't fill in "Skype IM" field     """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_PSIADFD(self):
        """035 - Press "Skype IM" field but  don't fill data """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(By.ID, "txtSkypeIM").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FIU2(self):
        """036 - Fill valid "Skype IM" """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtSkypeIM").send_keys(self.taxcode)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
    
    def test_DFZ(self):
        """037 - Don't fill in "zalo" field      """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_PDFZ(self):
        """038 - Press "zalo" field but  don't fill data"""
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(By.ID, "txtZalo").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FTZ(self):
        """039 - Fill text in Zalo  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtZalo").send_keys("a")
        assert True
    
    def test_FPNR(self):
        """040 - Fill phone number not register zalo   """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtZalo").send_keys(self.notregisterphone)
        self.press_save_button()
        error = self.driver.find_elements(By.CLASS_NAME, "tblInfo")[1].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[5].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n nh???p S??T ???? ????ng k?? zalo")

    def test_FPNNR(self):
        """041 - Fill phone number registered zalo """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtZalo").send_keys(self.phone)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_DFV(self):
        """042 - Don't fill in "Viber" field      """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_PFVDFD(self):
        """043 - Press "Viber" field but  don't fill data"""
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(By.ID, "txtViber").click()
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")

    def test_FTIV(self):
        """044 - Fill text in Viber  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtViber").send_keys("a")
        assert True

    def test_FPNVB(self):
        """045 - Fill phone number not register Viber  """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtViber").send_keys(self.notregisterphone)
        self.press_save_button()
        error = self.driver.find_elements(By.CLASS_NAME, "tblInfo")[1].find_element(By.TAG_NAME, "tbody").find_elements(
            By.TAG_NAME, "tr")[5].find_elements(By.TAG_NAME, "td")[1].find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(error == "B???n c???n nh???p S??T ???? ????ng k?? Viber")

    def test_FPVB(self):
        """046 - Fill phone number registered Viber """
        self.login_and_goto_profile()
        self.clearData()
        self.select_default_field()
        self.default_name()
        self.driver.find_element(
            By.ID, "txtViber").send_keys(self.phone)
        self.press_save_button()
        sucess_notification = self.driver.find_element(By.ID, "MainContent__userPage_ctl00_plInform").find_element(
            By.TAG_NAME, "span").get_attribute('innerHTML')
        self.assertTrue(sucess_notification ==
                        "Thay ?????i th??ng tin th??nh c??ng !")
    
    def test_DW15(self):
        """001"""
        self.login_and_goto_profile()
        time.sleep(15*60)
        assert False




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

