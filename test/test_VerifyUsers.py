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

class VerifyUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_verify_users(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("admin")
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("admin")
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/verify-users-0.png")
        time.sleep(2)
        
        driver.find_element(By.ID,"submit").click()
        
        # vérification de l'utilisateur loggé
        user = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]").text
        #print("User: ",user)
        
        # récupération de la liste des comptes créés
        # vérification que les comptes olivier et florian existent
        users = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/table[1]/tbody[1]/tr/td[2]")
        str_users = []
        for user in users:
            str_users.append(user.text)
        print("User: ",str_users)
        alive = False
        if ("olivier" in str_users) & ("flodrt" in str_users): alive = True
        time.sleep(2)
        driver.save_screenshot("./data/verify-users-1.png")
        time.sleep(2)
        assert alive == True, "Les utilisateurs créés olivier et florian ne sont pas présents"

        #logout
        driver.find_element(By.LINK_TEXT,"Logout").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/verify-users-2.png")
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
