from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ChoosePicker(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True

    def choose_picker(self):
        print "Choosing Picker data ... \n"        
        driver = self.driver
        driver.get("http://vodka.xwork.co/id/room-detail/ruang-meeting-di-wisma-76-spaces-254")
        driver.find_element_by_xpath("//div[@onclick=\"switchBookTab('harian')\"]").click()
        driver.find_element_by_xpath("//div[@onclick=\"switchBookTab('bulanan')\"]").click()
        driver.find_element_by_xpath("//div[@onclick=\"switchBookTab('perjam')\"]").click()
        driver.find_element_by_id("xwork-date-perjam").click()
        driver.find_element_by_xpath("//div[11]/div[3]/ul[3]/li[19]").click()
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[3]/div[4]/div[2]/div/div[2]/div[2]/button/span").click()
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[3]/div[4]/div[2]/div/div[2]/div[2]/div/ul/li[5]/a/span").click()
        Select(driver.find_element_by_id("date-perjam-start")).select_by_visible_text("12:00")
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[3]/div[4]/div[2]/div/div[3]/div[2]/button/span").click()
        driver.find_element_by_link_text("18:00").click()
        Select(driver.find_element_by_id("date-perjam-end")).select_by_visible_text("18:00")
        assert "Not Found" not in driver.page_source

    def is_element_present(self, how, what):
        print "Testing Success !"
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def is_alert_present(self):
        print "Testing Failed !"
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            print "Testing Success !"
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()        