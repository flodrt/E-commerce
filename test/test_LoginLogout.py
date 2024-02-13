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

class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        

    
    def test_login_logout(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("olivier")
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("passwd")
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/login-user-0.png")
        time.sleep(2)
        
        driver.find_element(By.ID,"submit").click()
        
        # vérification de l'utilisateur loggé
        user = driver.find_element(By.XPATH, "/html/body/nav/div/ul[2]/li[2]/a/b").text
        #print("User: ",user)
        
        time.sleep(2)
        driver.save_screenshot("./data/login-user-1.png")
        time.sleep(2)
        assert user == "Olivier", "L'utilisateur loggé n'est pas Olivier"

        driver.find_element(By.LINK_TEXT,"Logout").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/login-user-2.png")
        time.sleep(2)
        
        # vérification qu'on est bien sur la page d'accueil (Login)
        elt = driver.find_elements(By.LINK_TEXT,"Login")
        #print("Len: ",len(elt))
        assert len(elt) == 1, "L'utilisateur n'est pas déloggé"
    
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
