import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors= []
        self.accept_next_alert= True

    def test_login(self):
        driver = self.driver
        driver.get("http://bourbon.xwork.co/")
        driver.find_element_by_id("headerTitleContainer").click()
        driver.find_element_by_css_selector("h1.header-home-title").click()
        
        assert "No results found." not in driver.page_source
        
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
        self.driver.close()
		self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    unittest.main()