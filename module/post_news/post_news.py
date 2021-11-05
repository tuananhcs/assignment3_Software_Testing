
# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# import os
# from os import getcwd
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# driver.get("https://batdongsan.vn/dang-tin")



from re import match
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
        # PATH = "C:\Program Files (x86)\chromedriver.exe"
        # self.driver = webdriver.Chrome(PATH)
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.set_page_load_timeout(10)
        # self.driver.set_script_timeout(10)
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")
        self.driver.get("https://batdongsan.com.vn/dang-tin-rao-vat-ban-nha-dat")

    def pressSubmit(self):
        # buttonSubmit = self.driver.find_element(By.LINK_TEXT, "Gửi yêu cầu")
        # buttonSubmit.click()
        
        sb= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$btnSave']")
        sb.click()
        # time.sleep(1)
        

    def check_tieude(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[contains(text(),'Số ký tự cần lớn hơn 30')]")
        if len(sb) == 1:
            return False
        return True
    
    def check_dientich(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='postrow product-description']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True


    def check_thongtin(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//p[contains(text(),'Vui lòng nhập tiêu đề tin đăng của bạn. Tối thiểu ')]")
        if len(sb) == 1:
            return False
        return True

    def check_mattien(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='postrow product-description']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True

    def check_duongvao(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='leftArea leftPostArea']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True

    def check_phongngu(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='leftArea leftPostArea']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True

    def check_sotang(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='leftArea leftPostArea']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True

    def check_toilet(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//div[@class='leftArea leftPostArea']//div[@class='errorMessage']//p")
        if len(sb) == 1:
            return False
        return True

    def check_didong(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//body/form[@id='form1']/div[4]/div[3]/div[5]/div[1]/div[3]/div[12]/div[1]/div[4]/div[2]/span[1]")
        if len(sb) == 1:
            return False
        return True

    def check_email(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//span[contains(text(),'Vui lòng nhập đúng định dạng Email')]")
        if len(sb) == 1:
            return False
        return True
    

    def fillForm(self, tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email):
        text_true = "lasfkjasdfiawjeorqwieruqowejflaskjvlzkxjcvlsidufoiqwjelakjsdlf"
        text_false = "x"
        num_true = 155
        num_false = 2.4
        phone = "0820174291"
        emailfalse = "abc"
        emailtrue = "abc@gmail.com"
        # if (x):
        #     img = self.driver.find_element(By.XPATH,"//div[@class='upload']//input[@class='select']")
        #     img.send_keys(os.getcwd() + "/Untitled.png")
        # tieu de
        if tieude:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']")
            l.send_keys(text_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']")
            l.send_keys(text_false)
        # dien tich
        if dientich:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtArea']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtArea']")
            l.send_keys(num_false)

        # thong tin
        if thongtin:
            l= self.driver.find_element(By.XPATH,"//textarea[@name='ctl00$LeftMainContent$GuestProductInsert$txtDescription']")
            l.send_keys(text_true)
        else:
            l= self.driver.find_element(By.XPATH,"//textarea[@name='ctl00$LeftMainContent$GuestProductInsert$txtDescription']")
            l.send_keys("")
        
        # mat tien
        if mattien:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtWidth']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtWidth']")
            l.send_keys(num_false)

        # duong vao
        if duongvao:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtLandWidth']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtLandWidth']")
            l.send_keys(num_false)
        
        # so tang
        if sotang:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtFloorNumbers']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtFloorNumbers']")
            l.send_keys(num_false)

        # so phong ngu
        if phongngu:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtRoomNumber']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtRoomNumber']")
            l.send_keys(num_false)

        # toilet
        if toilet:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtToiletNumber']")
            l.send_keys(num_true)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtToiletNumber']")
            l.send_keys(num_false)

        # di dong
        if didong:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtBrMobile']")
            l.send_keys(phone)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtBrMobile']")
            l.send_keys("")


        # email
        if email:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtBrEmail']")
            l.send_keys(emailtrue)
        else:
            l= self.driver.find_element(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtBrEmail']")
            l.send_keys(emailfalse)

        
        self.pressSubmit()
        # time.sleep(3)
        

        #get_attribute() to get value of input box
        # self.pressSubmit()
    
    
    def rest(self):
        
        time.sleep(2)


    def test_NT1(self):
        tieude = False
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertFalse(self.check_tieude())

    def test_T1(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_tieude())

    def test_TNN1(self):
        tieude = True
        dientich = False
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_dientich())

    def test_TN1(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_dientich())

    def test_NT2(self):
        tieude = True
        dientich = True
        thongtin = False
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_thongtin())

    def test_T2(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_thongtin())

    def test_TN3(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_mattien())

    def test_TNN3(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = False
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_mattien())

    def test_TN6(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_phongngu())

    def test_TNN6(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = False
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_phongngu())

    def test_TN4(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_duongvao())

    def test_TNN4(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = False
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_duongvao())

    def test_TN5(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_sotang())

    def test_TNN5(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = False
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_sotang())

    def test_TN8(self):
        tieude = False
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_toilet())

    def test_TNN7(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = False
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_toilet())

    def test_TN9(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertFalse(self.check_didong())

    def test_TNN9(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = False
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertFalse(self.check_didong())

    def test_TA(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = True
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)

        self.assertTrue(self.check_email())

    def test_TNA(self):
        tieude = True
        dientich = True
        thongtin = True
        mattien = True
        phongngu = True
        duongvao = True
        sotang = True
        toilet = True
        didong = True
        email = False
        self.fillForm(tieude,dientich,thongtin,mattien,duongvao,phongngu,sotang,toilet,didong,email)
        time.sleep(1)
        self.assertTrue(self.check_email())

    


    def tearDown(self):
        # time.sleep(3)
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
