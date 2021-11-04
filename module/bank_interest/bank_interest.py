
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
        self.driver.get("https://batdongsan.com.vn/ho-tro-tien-ich/ht-tinh-lai-suat")

    def pressSubmit(self):
        # buttonSubmit = self.driver.find_element(By.LINK_TEXT, "Gửi yêu cầu")
        # buttonSubmit.click()
        
        sb= self.driver.find_element(By.XPATH,"//input[@value='Xem kết quả']")
        sb.click()

    def check_money(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//form[@novalidate='novalidate']/div[1]/div[1]/div[1]/span[1]/span[1]")
        return len(sb) == 0
    
    def check_time(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//form[@novalidate='novalidate']/div[2]/div[1]/div[2]/span[1]/span[1]")
        return len(sb) == 0

    def check_interest(self):
        # sb= self.driver.find_elements(By.XPATH,"//input[@name='ctl00$LeftMainContent$GuestProductInsert$txtProductTitle']/following-sibling::div[0]/p")
        sb = self.driver.find_elements(By.XPATH,"//form[@novalidate='novalidate']/div[3]/div[1]/div[2]/span[1]/span[1]")
        return len(sb) == 0

    def check_all(self):
        return self.check_interest() and self.check_money() and self.check_time()    
    
    def fillForm(self, money,time,timetype,interest,interesttype,paytype):
        money1 = 10000000
        money2 = "abc"
        time1 = 12
        time2 = 1.2
        time3 = "abc"
        interest1 = 6
        interest2 = 2.4
        interest3 = "aco"
        # if (x):
        #     img = self.driver.find_element(By.XPATH,"//div[@class='upload']//input[@class='select']")
        #     img.send_keys(os.getcwd() + "/Untitled.png")
        # money
        if money == 1:
            l= self.driver.find_element(By.XPATH,"//input[@id='txtAmount']")
            l.send_keys("")
        elif money == 2:
            l= self.driver.find_element(By.XPATH,"//input[@id='txtAmount']")
            l.send_keys(money2)
        elif money == 3:
            l= self.driver.find_element(By.XPATH,"//input[@id='txtAmount']")
            l.send_keys(money1)


        # time
        if time == 1:
            l= self.driver.find_element(By.XPATH,"//input[@id='Period']")
            l.send_keys("")
        elif time == 2:
            l= self.driver.find_element(By.XPATH,"//input[@id='Period']")
            l.send_keys(time3)
        elif time == 3:
            l= self.driver.find_element(By.XPATH,"//input[@id='Period']")
            l.send_keys(time1)
        elif time == 4:
            l= self.driver.find_element(By.XPATH,"//input[@id='Period']")
            l.send_keys(time2)

        #timetype
        if timetype:
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']").click()
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']/option[text()='Tháng']").click()
        else:
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']").click()
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']/option[text()='Năm']").click()

        # interest
        if interest == 1:
            l= self.driver.find_element(By.XPATH,"//input[@id='Rate']")
            l.send_keys("")
        elif interest == 2:
            l= self.driver.find_element(By.XPATH,"//input[@id='Rate']")
            l.send_keys(interest3)
        elif interest == 3:
            l= self.driver.find_element(By.XPATH,"//input[@id='Rate']")
            l.send_keys(interest1)
        elif interest == 4:
            l= self.driver.find_element(By.XPATH,"//input[@id='Rate']")
            l.send_keys(interest2)

        
        #interestType
        if interesttype:
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']").click()
            self.driver.find_element(By.XPATH,"//select[@id='PeriodType']/option[text()='Tháng']").click()
        else:
            self.driver.find_element(By.XPATH,"//select[@id='InterestType']").click()
            self.driver.find_element(By.XPATH,"//select[@id='InterestType']/option[text()='Năm']").click()
        

        # paytype
        if paytype :
            self.driver.find_element(By.XPATH,"//select[@id='PayingInterestType']").click()
            self.driver.find_element(By.XPATH,"//select[@id='PayingInterestType']/option[1]").click()

        self.pressSubmit()

        #get_attribute() to get value of input box
        # self.pressSubmit()
    
    
    def rest(self):
        
        time.sleep(2)


    def test_M0(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 1
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_money())

    def test_Mc(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 2
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_money())

    def test_Mn(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_money())

    def test_LT0(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 1
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_time())

    def test_LTc(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 2
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_time())

    def test_LTn(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_time())

    def test_LTr(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not    
        money = 3
        time = 4
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_time())

    def test_I0(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 1
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_interest())

    def test_Ic(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 2
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertFalse(self.check_interest())

    def test_Iint(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_interest())

    def test_Inon_int(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 4
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_interest())

    def test_LTy(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = False
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())

    def test_LTm(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())

    def test_ITy(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = False
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())

    def test_ITm(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())

    def test_PT0(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())

    def test_PTc(self):
        # money = 1: not type, 2: non-number, 3: number
        # time = 1: not type, 2: non-number, 3: number, 4: realnum
        # timeType = True: month, False: year
        # interest = 1: not type, 2: non-number, 3: number, 4: realnum
        # interestType = True: month, False: year
        # paytype = True: choose, False: not
        money = 3
        time = 3
        timetype = True
        interest = 3
        interesttype = True
        paytype = True
        self.fillForm(money,time,timetype,interest,interesttype,paytype)
        self.assertTrue(self.check_all())


    
    


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
