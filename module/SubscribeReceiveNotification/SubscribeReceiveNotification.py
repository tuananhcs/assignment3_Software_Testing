import time
import os
import unittest
from unittest import result
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DetailedEstimate(unittest.TestCase):
    def setUp(self):
        cService = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=options, service=cService)
        # self.driver.implicitly_wait(3)
        self.driver.get("https://batdongsan.com.vn/can-mua-can-thue")

        print("[Open browser] Open google chrome browser")

        print("========== [Begin Test] ==========")

    def functionAccess(self):
        first = self.driver.find_element(By.XPATH, '//div[@class="Main"]/div[2]/div[@class="p-title"]/a')
        first.click()

        emailregister = self.driver.find_element(By.ID, 'emailregister')
        emailregister.click()
        time.sleep(3)

    def pressSubmit(self):
        buttonSubmit = self.driver.find_element(By.XPATH, './/button[@id="btnRegister"]')
        buttonSubmit.click()

    def confirmAlert(self):
        alert_displayed = False
        try:
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.alert_is_present(), "Alert not show")
            alert_displayed = True
        except:
            pass
        if alert_displayed == False:
            return False
        
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        return True

    def input_email_letter_frequency(self, email_letter_frequency):
        email_letter_frequency_field = self.driver.find_element(By.XPATH, './/table[@id="rblFrequency"]')
        email_letter_frequency_values = email_letter_frequency_field.find_elements(By.XPATH, './/input[@id="EmailLetter_Frequency"]')
        email_letter_frequency_values[email_letter_frequency].click()
        time.sleep(1)

    def input_category(self, category):
        # divCategoryRegisterEmailSale
        category_field = self.driver.find_element(By.ID, 'divCategoryRegisterEmailSale')
        category_field.click()
        category_values = category_field.find_elements(By.XPATH, '//div[@id="divCategoryRegisterEmailSaleOptions"]/ul/li')
        category_values[category].click()
        time.sleep(1)

    def input_category_re(self, category_re):
        # divCategoryReRegisterEmailSale
        category_re_field = self.driver.find_element(By.ID, 'divCategoryReRegisterEmailSale')
        category_re_field.click()
        category_re_values = category_re_field.find_elements(By.XPATH, '//div[@id="divCategoryReRegisterEmailSaleOptions"]/ul/li')
        category_re_values[category_re].click()
        time.sleep(1)

    def input_city(self, city):
        # divCityCodeRegisterEmailSale
        city_field = self.driver.find_element(By.ID, 'divCityCodeRegisterEmailSale')
        city_field.click()
        city_values = city_field.find_elements(By.XPATH, '//div[@id="divCityCodeRegisterEmailSaleOptions"]/ul/li')
        city_values[city].click()
        time.sleep(1)

    def input_district(self, district):
        # divDistrictIdRegisterEmailSale
        district_field = self.driver.find_element(By.ID, 'divDistrictIdRegisterEmailSale')
        district_field.click()
        district_values = district_field.find_elements(By.XPATH, '//div[@id="divDistrictIdRegisterEmailSaleOptions"]/ul/li')
        district_values[district].click()
        time.sleep(1)

    def input_area(self, area):
        # divAreaRegisterEmailSale
        area_field = self.driver.find_element(By.ID, 'divAreaRegisterEmailSale')
        area_field.click()
        area_values = area_field.find_elements(By.XPATH, '//div[@id="divAreaRegisterEmailSaleOptions"]/ul/li')
        area_values[area].click()
        time.sleep(1)

    def input_price(self, price):
        # divPriceRegisterEmailSale
        price_field = self.driver.find_element(By.ID, 'divPriceRegisterEmailSale')
        price_field.click()
        price_values = price_field.find_elements(By.XPATH, '//div[@id="divPriceRegisterEmailSaleOptions"]/ul/li')
        price_values[price].click()
        time.sleep(1)

    def input_ward(self, ward):
        # divWardRegisterEmailSale
        ward_field = self.driver.find_element(By.ID, 'divWardRegisterEmailSale')
        ward_field.click()
        ward_values = ward_field.find_elements(By.XPATH, '//div[@id="divWardRegisterEmailSaleOptions"]/ul/li')
        ward_values[ward].click()
        time.sleep(1)

    def input_street(self, street):
        # divStreetRegisterEmailSale
        street_field = self.driver.find_element(By.ID, 'divStreetRegisterEmailSale')
        street_field.click()
        street_values = street_field.find_elements(By.XPATH, '//div[@id="divStreetRegisterEmailSaleOptions"]/ul/li')
        street_values[street].click()
        time.sleep(1)

    def input_room(self, room):
        # divRoomRegisterEmailSale
        room_field = self.driver.find_element(By.ID, 'divRoomRegisterEmailSale')
        room_field.click()
        room_values = room_field.find_elements(By.XPATH, '//div[@id="divRoomRegisterEmailSaleOptions"]/ul/li')
        room_values[room].click()
        time.sleep(1)

    def input_direction(self, direction):
        # divDirectionRegisterEmailSale
        direction_field = self.driver.find_element(By.ID, 'divDirectionRegisterEmailSale')
        direction_field.click()
        direction_values = direction_field.find_elements(By.XPATH, '//div[@id="divDirectionRegisterEmailSaleOptions"]/ul/li')
        direction_values[direction].click()
        time.sleep(1)

    def input_project(self, project):
        # divProjectRegisterEmailSale
        project_field = self.driver.find_element(By.ID, 'divProjectRegisterEmailSale')
        project_field.click()
        project_values = project_field.find_elements(By.XPATH, '//div[@id="divProjectRegisterEmailSaleOptions"]/ul/li')
        project_values[project].click()
        time.sleep(1)
    
    def input_code(self, code):
        # codeRegister
        code_field = self.driver.find_element(By.ID, 'codeRegister')
        code_field.send_keys(code)
        time.sleep(1)

    def input_txt_title(self, txt_title):
        # txtTitle
        txt_title_field = self.driver.find_element(By.ID, 'txtTitle')
        txt_title_field.send_keys(txt_title)
        time.sleep(1)

    def input_text_email(self, text_email):
        # txtEmail
        text_email_field = self.driver.find_element(By.ID, 'txtEmail')
        text_email_field.send_keys(text_email)
        time.sleep(1)

    def input_name(self, name):
        # name
        name_field = self.driver.find_element(By.ID, 'name')
        name_field.send_keys(name)
        time.sleep(1)

    def fillForm(self, email_letter_frequency, category, category_re, city, district, area, 
        price, ward, street, room, direction, project, code, txt_title, text_email, name):

        if email_letter_frequency != None:
            self.input_email_letter_frequency(email_letter_frequency)

        if category != None:
            self.input_category(category)

        if category_re != None:
            self.input_category_re(category_re)

        if city != None:
            self.input_city(city)

        if district != None:
            self.input_district(district)

        if area != None:
            self.input_area(area)

        if price != None:
            self.input_price(price)

        if ward != None:
            self.input_ward(ward)        

        if street != None:
            self.input_street(street)

        if room != None:
            self.input_room(room)        

        if direction != None:
            self.input_direction(direction)

        if project != None:
            self.input_project(project)

        if code != None:
            self.input_code(code)

        if txt_title != None:
            self.input_txt_title(txt_title)

        if text_email != None:
            self.input_text_email(text_email)

        if name != None:
            self.input_name(name)

        self.pressSubmit()
        time.sleep(3)
    
    def test_TSNTT1(self):
        self.functionAccess()
        self.fillForm(None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_TSNTT2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_LTR1(self):
        self.functionAccess()
        category_field = self.driver.find_element(By.ID, 'divCategoryRegisterEmailSale')
        category_field.click()
        category_values = category_field.find_elements(By.XPATH, '//div[@id="divCategoryRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(category_values) > 1)

    def test_LTR2(self):
        self.functionAccess()
        self.fillForm(2, None, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_LTR3(self):
        self.functionAccess()
        self.fillForm(2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_LTR4(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_LND1(self):
        self.functionAccess()
        category_re_field = self.driver.find_element(By.ID, 'divCategoryReRegisterEmailSale')
        category_re_field.click()
        category_re_values = category_re_field.find_elements(By.XPATH, '//div[@id="divCategoryReRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(category_re_values) > 1)

    def test_LND2(self):
        self.functionAccess()
        self.input_category(2)
        category_re_field = self.driver.find_element(By.ID, 'divCategoryReRegisterEmailSale')
        category_re_field.click()
        category_re_values = category_re_field.find_elements(By.XPATH, '//div[@id="divCategoryReRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(category_re_values) > 1)

    def test_LND3(self):
        self.functionAccess()
        self.fillForm(2, 0, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_LND4(self):
        self.functionAccess()
        self.fillForm(2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_LND5(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_TTP1(self):
        self.functionAccess()
        city_field = self.driver.find_element(By.ID, 'divCityCodeRegisterEmailSale')
        city_field.click()
        city_values = city_field.find_elements(By.XPATH, '//div[@id="divCityCodeRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(city_values) > 1)

    def test_TTP2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, None, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_TTP3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_TTP4(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_QH1(self):
        self.functionAccess()
        district_field = self.driver.find_element(By.ID, 'divDistrictIdRegisterEmailSale')
        district_field.click()
        district_values = district_field.find_elements(By.XPATH, '//div[@id="divDistrictIdRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(district_values) > 1)

    def test_QH2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, None, None, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_QH3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 2, 0, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertFalse(self.confirmAlert())

    def test_QH4(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_QH5(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, None, None, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())
    
    def test_DT1(self):
        self.functionAccess()
        area_field = self.driver.find_element(By.ID, 'divAreaRegisterEmailSale')
        area_field.click()
        area_values = area_field.find_elements(By.XPATH, '//div[@id="divAreaRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(area_values) > 1)

    def test_DT2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, None, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_DT3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_MG1(self):
        self.functionAccess()
        price_field = self.driver.find_element(By.ID, 'divPriceRegisterEmailSale')
        price_field.click()
        price_values = price_field.find_elements(By.XPATH, '//div[@id="divPriceRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(price_values) > 1)

    def test_MG2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, None, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_MG3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_PX1(self):
        self.functionAccess()
        ward_field = self.driver.find_element(By.ID, 'divWardRegisterEmailSale')
        ward_field.click()
        ward_values = ward_field.find_elements(By.XPATH, '//div[@id="divWardRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(ward_values) > 1)

    def test_PX2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, None, None, 2, 2, None, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_PX3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_DP1(self):
        self.functionAccess()
        street_field = self.driver.find_element(By.ID, 'divStreetRegisterEmailSale')
        street_field.click()
        street_values = street_field.find_elements(By.XPATH, '//div[@id="divStreetRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(street_values) > 1)

    def test_DP2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, None, None, 2, 2, None, None, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_DP3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_SPN1(self):
        self.functionAccess()
        room_field = self.driver.find_element(By.ID, 'divRoomRegisterEmailSale')
        room_field.click()
        room_values = room_field.find_elements(By.XPATH, '//div[@id="divRoomRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(room_values) > 1)

    def test_SPN2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_SPN3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_HN1(self):
        self.functionAccess()
        direction_field = self.driver.find_element(By.ID, 'divDirectionRegisterEmailSale')
        direction_field.click()
        direction_values = direction_field.find_elements(By.XPATH, '//div[@id="divDirectionRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(direction_values) > 1)

    def test_HN2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_HN3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_DABDS1(self):
        self.functionAccess()
        project_field = self.driver.find_element(By.ID, 'divProjectRegisterEmailSale')
        project_field.click()
        project_values = project_field.find_elements(By.XPATH, '//div[@id="divProjectRegisterEmailSaleOptions"]/ul/li')
        self.assertTrue(len(project_values) > 1)

    def test_DABDS2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_DABDS3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_MAT1(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())
            

    def test_MAT2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "AAAA", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@for="codeRegister"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn vui lòng nhập đúng mã an toàn")

    def test_MAT3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@for="codeRegister"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn vui lòng nhập mã an toàn")

    def test_MAT4(self):
        self.functionAccess()
        code_image_source1 = self.driver.find_element(By.ID, 'secodeRegister').get_attribute('src')
        button_reload_captcha = self.driver.find_element(By.ID, 'reloadCaptchaRegister')
        button_reload_captcha.click()
        time.sleep(1)
        code_image_source2 = self.driver.find_element(By.ID, 'secodeRegister').get_attribute('src')
        self.assertFalse(code_image_source1 == code_image_source2)
        
    def test_TDT1(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@for="txtTitle"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn vui lòng điền tiêu đề thư")

    def test_TDT2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_ENTB1(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@for="txtEmail"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn vui lòng điền email nhận thông báo")

    def test_ENTB2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@for="txtEmail"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn nhập sai định dạng mail")

    def test_ENTB3(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_HT1(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "")
        self.assertTrue(self.confirmAlert())

    def test_HT2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_SP1(self):
        self.functionAccess()
        self.fillForm(2, 2, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@data-valmsg-for="EmailLetter.CateId"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "Bạn vui lòng chọn loại nhà đất")

    def test_SP2(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == True:
            self.assertTrue(False)
        error_message = self.driver.find_element(By.XPATH, '//span[@data-valmsg-for="EmailLetter.Rooms"]')
        self.assertTrue(error_message.get_attribute('innerHTML') == "The value '-1' is not valid for Rooms.")

    def test_SC1(self):
        self.functionAccess()
        self.fillForm(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        if self.confirmAlert() == False:
            self.assertTrue(False)
        try:
            self.driver.find_element(By.ID, 'pnlRegister')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_SC2(self):
        self.functionAccess()
        self.fillForm(2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, "3LJX", "Nhận thư báo", "test@gmail.com", "Nam Huỳnh")
        self.assertTrue(self.confirmAlert())

    def test_RL1(self):
        self.functionAccess()
        self.driver.refresh()
        try:
            self.driver.find_element(By.ID, 'pnlRegister')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_CF1(self):
        self.functionAccess()

    def tearDown(self):
        self.driver.quit()
        print("========== [End Test] ==========\n")

if __name__ == "__main__":
    unittest.main()
