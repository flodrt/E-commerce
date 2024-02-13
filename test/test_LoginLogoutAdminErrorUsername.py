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

class LoginLogoutAdminErrorUsername(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_logout_admin_error_username(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("adm")
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("admin")
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/login-admin-error-username-0.png")
        time.sleep(2)
        
        driver.find_element(By.ID,"submit").click()
        
        # vérification de l'utilisateur loggé
        msg = driver.find_element(By.XPATH, "//body/div[1]").text
        msg = msg[2:]
        #print("User: ",msg)
        
        #verification de la presence du message d'erreur
        time.sleep(2)
        driver.save_screenshot("./data/login-admin-error-username-1.png")
        time.sleep(2)
        assert msg == "Username and password are not match! Please try again", "La détection d'erreur de mot de passe ne fonctionne pas"

                  
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
