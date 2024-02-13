# -*- coding: utf-8 -*-
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import unittest
import os

class TestLoginLogout(unittest.TestCase):

    def setUp(self):

        lt_options = {
            "user": "drouotflorian",
            "accessKey": "aXEhocGpX9blNZw7bNFVRyDKGhHtpwkjxMXZPPkVDvBio5mZ9r",
            "build": "UnitTest-Selenium-Sample",
            "name": "UnitTest-Selenium-Test",
            "platformName": "Windows 11",
            "w3c": True,
            "browserName": "Chrome",
            "browserVersion": "latest",
            "selenium_version": "4.8.0"
        }
        
        browser_options = ChromeOptions()
        browser_options.set_capability('LT:Options', lt_options)

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)
    
    def test_loggin(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::div[1]").click()
        driver.find_element(By.LINK_TEXT, "Getting Started").click()
        # driver.find_element(By.ID,"username").click()
        # driver.find_element(By.ID,"username").clear()
        # driver.find_element(By.ID,"username").send_keys("flodrt")
        # driver.find_element(By.ID,"password").click()
        # driver.find_element(By.ID,"password").clear()
        # driver.find_element(By.ID,"password").send_keys("f")
        # driver.find_element(By.ID,"submit").click()   
        
        driver.find_element(By.XPATH, "//body").click()
        driver.find_element(By.XPATH, "//body").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("f")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("floflo")
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
        # driver.save_screenshot('.\TEST_ProjetFilRouge\LoginUser\Screenshots\MessageErreurMauvaisID.png')
        # TEST comparatif 
        self.assertEqual (msgErreur, ValeurAttendue  )
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
