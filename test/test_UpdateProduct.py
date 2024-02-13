# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

opts = ChromeOptions()
opts.add_argument("--start-maximized")

class UpdateProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_update_product(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element(By.LINK_TEXT,"Getting Started").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("admin")
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("admin")
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"submit").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/update-product-0.png")
        time.sleep(2)
        
        # récupération de l'item avant update
        bef_items = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td")
    
        #print("Item before: ",bef_items[1].text)
        
        #update d'un item
        driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='olivier'])[1]/following::button[1]").click()
        
        #récupération de l'item aprés updater
        aft_items = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td")
    
        #print("Item after: ",aft_items[1].text)
        
        eg=True
        for i in range(len(aft_items)):
            if (bef_items[i].text != aft_items[i].text): eg=False
                
        
        time.sleep(2)
        driver.save_screenshot("./data/update-product-1.png")
        time.sleep(2)
        
        assert eg != True, "La mise à jour n'a pas été effectuée"
        
        time.sleep(2)
        driver.save_screenshot("./data/update-product-2.png")
        time.sleep(2)
        #logout
        driver.find_element(By.LINK_TEXT,"Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
