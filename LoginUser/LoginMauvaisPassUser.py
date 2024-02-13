# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Loggin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_loggin(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::div[1]").click()
        driver.find_element(By.LINK_TEXT, "Getting Started").click()
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("flodrt")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("f")
        driver.find_element(By.ID,"submit").click()

        #Recuperation message erreur
        msgErreur = driver.find_element(By.XPATH, "//body/div[1]").text
        print("----------------------------------------------------------------")
        msgErreur = msgErreur [2:]
        print (msgErreur)
        ValeurAttendue="Username and password are not match! Please try again"
        print (ValeurAttendue)
        print ("------------------------------------------------")
        # SCREENSHOT 
        driver.save_screenshot('.\TEST_ProjetFilRouge\LoginUser\Screenshots\MessageErreurMauvaisPass.png')
        # TEST comparatif 
        self.assertEqual (msgErreur, ValeurAttendue  )

        driver.find_element(By.XPATH, "//body").click()
        driver.find_element(By.XPATH, "//body").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("f")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("floflo")
        driver.find_element(By.ID,"submit").click()
    
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
