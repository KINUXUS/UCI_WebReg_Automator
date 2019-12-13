from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def _show_study_list(self, xpath="//input[@value='Show Study List']"):
    self._wait_until_present(By.XPATH, xpath)
    button = self.driver.find_element_by_xpath(xpath)
    button.click()


def get_study_list(self, xpath="//table[0]/tbody/tr[2]/td"):
    self._wait_until_present(By.XPATH, xpath)
    return self.driver.find_element_by_xpath(xpath).text

def _get_study_list_table_title(self, xpath="//table[0]/tbody/tr[1]/th/h2"):
    self._wait_until_present(By.XPATH, xpath)
    return self.driver.find_element_by_xpath(xpath).text
