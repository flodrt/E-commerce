# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re

class CreateAccountWithNoId(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_account_with_no_id(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element(By.LINK_TEXT, "Getting Started").click()
        driver.find_element(By.LINK_TEXT, "Create Account").click()
        driver.find_element(By.ID,"email_address").click()
        driver.find_element(By.ID,"email_address").clear()
        driver.find_element(By.ID,"email_address").send_keys("qrehgsqeht@hoymail.fr")
        driver.find_element(By.ID,"password1").click()
        driver.find_element(By.ID,"password1").clear()
        driver.find_element(By.ID,"password1").send_keys("floflo")
        driver.find_element(By.ID,"password2").click()
        driver.find_element(By.ID,"password2").clear()
        driver.find_element(By.ID,"password2").send_keys("floflo")
        driver.find_element(By.ID,"submit").click()

        # Attendre que le message d'erreur soit visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))

        # Récupérer le message d'erreur
        msgErreur = driver.find_element(By.CLASS_NAME, "alert-danger").text
        
        print("----------------------------------------------------------------")
        print (msgErreur)
        ValeurAttendue = "There was an error with creating a user: ['Field must be equal to password1.']"
        print (ValeurAttendue)
        print ("------------------------------------------------")

        # TEST comparatif 
        self.assertEqual (msgErreur, ValeurAttendue  )
    
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
