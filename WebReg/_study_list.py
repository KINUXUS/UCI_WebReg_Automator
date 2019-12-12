from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_study_list(self, xpath="//table[0]/tbody/tr[2]/td"):
    self._wait_until_present(By.XPATH, xpath)
    schedule = self.driver.find_element_by_xpath(xpath)
    return schedule.text
