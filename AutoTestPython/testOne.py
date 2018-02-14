from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://bourbon.xwork.co")
        driver.find_element_by_id("meeting-area").click()
        driver.find_element_by_xpath("//div[@id='login-btn']/span").click()
        driver.find_element_by_id("email-login-1").click()
        driver.find_element_by_id("email-login-1").send_keys("anjay@gmail.com")
        driver.find_element_by_id("password-login-1").send_keys("younglex18")
        driver.find_element_by_id("do-login").click()
        driver.find_element_by_xpath("//div[@id='header']/div/div[2]/div[2]/i").click()
        driver.find_element_by_xpath("//div[@id='user-dropdown']/a[5]/span").click()
        assert "Testing gagal.\n"." No results found." not in driver.page_source


    def tearDown(self):
    	print 'Testing Success\n' 
        self.driver.close()


if __name__ == "__main__":
    unittest.main()