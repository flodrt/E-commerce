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

class NavAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_nav_admin(self):
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
        driver.save_screenshot("./data/nav-admin-0.png")
        time.sleep(2)
        
        #nav vers page achat
        driver.find_element(By.LINK_TEXT,"Market").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-1.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h2[1]").text
        #print("Title: ", title)
        
        assert title == "Available Items", "Pb de navigation vers la fenêtre d'achat"
        
        
        #nav vers page admin
        driver.find_element(By.LINK_TEXT,"Admin Panel").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-2.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/h1[1]").text
        #print("Title: ", title)
        
        assert title == "Welcome to Admin Panel", "Pb de navigation vers Admin Panel"
        
        #nav vers page home
        driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-3.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h1[1]").text
        #print("Title: ", title)
        
        driver.find_element(By.LINK_TEXT,"Admin Panel").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-4.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/h1[1]").text
        #print("Title: ", title)
        
        assert title == "Welcome to Admin Panel", "Pb de navigation vers Admin Panel"
        
        
        #nav vers page accueil
        driver.find_element(By.LINK_TEXT,"E-Commerce").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-5.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h1[1]").text
        #print("Title: ", title)
        
        assert title == "E-Commerce Website", "Pb de navigation vers la fenêtre d'accueil"
        
        
        #nav vers page admin
        driver.find_element(By.LINK_TEXT,"Admin Panel").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-6.png")
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html[1]/body[1]/h1[1]").text
        #print("Title: ", title)
        
        assert title == "Welcome to Admin Panel", "Pb de navigation vers Admin Panel"
        
        
        #logout
        driver.find_element(By.LINK_TEXT,"Logout").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/nav-admin-7.png")
        time.sleep(2)
    
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
