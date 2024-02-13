# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AchatReventeTestConfirmationStockBudgetMessage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_achat_revente_test_confirmation_stock_budget_message(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::div[2]").click()
        driver.find_element(By.LINK_TEXT, "Getting Started").click()
        driver.find_element(By.ID,"username").click()
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys("flodrt")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("floflo")
        driver.find_element(By.ID,"submit").click()

        # SCREENSHOT 
        driver.save_screenshot('.\TEST_ProjetFilRouge\AchatReventePFR\Screenshots\BudgetAvAchat.png')
        #Recuperation Budget avant et prix de l'article en text  +  conversion en float 
        BudgetAv = driver.find_element(By.XPATH, "//body/nav[1]/div[1]/ul[2]/li[1]/a[1]").text
        BudgetAv = float(''.join(filter(str.isdigit, BudgetAv)))

        prix =driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]").text
        prix = float(''.join(filter(str.isdigit, prix)))
        
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Info'])[1]/following::button[1]").click()
        driver.find_element(By.ID,"submit").click()  
        # SCREENSHOT 
        driver.save_screenshot('.\TEST_ProjetFilRouge\AchatReventePFR\Screenshots\BudgetApAchat.png')

        #Recuperation Budget apres en text  +  conversion en float 
        BudgetAp = driver.find_element(By.XPATH, "//body/nav[1]/div[1]/ul[2]/li[1]/a[1]").text
        BudgetAp = float(''.join(filter(str.isdigit, BudgetAp)))

        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='IPhone 15'])[3]/following::button[1]").click()
        
        time .sleep(5)
        
        driver.find_element(By.XPATH, "//div[@id='Sell-1']/div/div/div[2]/form/div/input[2]").click()

        

        driver.find_element(By.LINK_TEXT, "Logout").click()


        #TEST GESTION DU BUDGET LORS D'UN ACHAT 
        print("----------------------------------------------------------------")
        print (BudgetAv)
        print (prix)
        print (BudgetAp)
        ValeurAttendue=BudgetAv-prix
        print (ValeurAttendue)
        print ("------------------------------------------------")
        # ASSERT
        self.assertEqual (BudgetAp, ValeurAttendue  )


    
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