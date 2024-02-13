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

        #Recuperation du nombre d'article dans le stock,  l'achat
        NbArticleStockAv = driver.find_elements(By.XPATH, "//tbody/tr")
        NbArticleStockAv= len (NbArticleStockAv)

        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Info'])[1]/following::button[1]").click()
        driver.find_element(By.ID,"submit").click()
        
        #Recuperation du nombre d'article dans le stock, apres l'achat
        NbArticleStockAp = driver.find_elements(By.XPATH, "//tbody/tr")
        NbArticleStockAp= len (NbArticleStockAp)

        #Recuperation du nombre d'article acheté
        NbArticleAchete = driver.find_elements(By.XPATH, "//body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]")
        NbArticleAchete= len (NbArticleAchete)

        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='IPhone 15'])[3]/following::button[1]").click()
        driver.find_element(By.XPATH, "//div[@id='Sell-1']/div/div/div[2]/form/div/input[2]").click()

        #Recuperation message confirmation d'achat
        msgConfirmationV = driver.find_element(By.XPATH, "//body/div[1]").text
        msgConfirmationV = msgConfirmationV [2:]

        driver.find_element(By.LINK_TEXT, "Logout").click()

        # #TEST Gestion du stock CONFIRMATION ACHAT 
        print("----------------------------------------------------------------")
        print (NbArticleStockAv)
        print (NbArticleAchete)
        print ( NbArticleStockAp)
        ValeurAttendue=NbArticleAchete+NbArticleStockAp
        print (ValeurAttendue)
        print ("------------------------------------------------")
        # # ASSERT
        self.assertEqual (NbArticleStockAv, ValeurAttendue  )

    
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
