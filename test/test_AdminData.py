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

class AdminData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin_data(self):
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
        driver.save_screenshot("./data/login-admin-data-0.png")
        time.sleep(2)
        
        driver.find_element(By.ID,"submit").click()
        
                
        # récupération de la liste des prix
        item_prices = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr/td[3]")
        count= len(item_prices)
        #print("Count before: ",count)
        #for item in item_prices:
        #    print("Item: ",item.text)
        
        # récupération de la liste des owners
        item_owners = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr/td[4]")
        count= len(item_owners)
        #print("Count before: ",count)
    
        #for item in item_owners:
        #    print("Owner: ",item.text)
            
        # récupération de la liste des comptes créés
        # vérification que les comptes olivier et florian existent
        users = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/table[1]/tbody[1]/tr/td[2]")
        #for user in users:
        #    print("User: ",user.text)
        
        budgets = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/table[1]/tbody[1]/tr/td[3]")
        #for budget in budgets:
        #    print("Budget: ",budget.text)
        
        carts = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/table[1]/tbody[1]/tr/td[4]")
        #for cart in carts:
        #    print("Cart: ",cart.text)
        
        users_count = len(users)
        #check the users data in control users table for empty carts
        for i in range(users_count):
            if users[i].text == "admin":
                assert carts[i].text == "Empty", "Pb sur caddie Admin"
                assert budgets[i].text == "0 $", "Pb sur budget Admin"
            else:
                if (carts[i].text == "Empty"):
                    assert budgets[i].text == "10,000 $", "Pb sur caddie de " + users[i].text
       
                
        #check the users data in control users table for non empty carts
        for i in range(users_count):
            if carts[i].text != "Empty":
                cart_value= int(((budgets[i].text).replace(",","")).replace("$",""))
                #print("Cart Value: ",cart_value)
                owner_count = 10000
                for j in range(count):
                    if users[i].text == item_owners[j].text:
                        owner_count = owner_count - int(((item_prices[j].text).replace(",","")).replace("$",""))
                #print("OWner Cart Value: ",owner_count)
                assert owner_count == cart_value, "Pb sur le budget " + users[i].text
        
        time.sleep(2)
        driver.save_screenshot("./data/login-admin-data-1.png")
        time.sleep(2)
        

        #logout
        driver.find_element(By.LINK_TEXT,"Logout").click()
        
        time.sleep(2)
        driver.save_screenshot("./data/login-admin-data-2.png")
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
