from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re


def _show_study_list(self, xpath="//input[@value='Show Study List']"):
    self._wait_until_present(By.XPATH, xpath)
    button = self.driver.find_element_by_xpath(xpath)
    button.click()


def _get_table_HTML(self, class_name="studyList", keyword='table') -> str:
    self._wait_until_present(By.CLASS_NAME, class_name)
    for table in self.driver.find_elements_by_class_name(class_name):
        outer_HTML = table.get_attribute('outerHTML')
        if not outer_HTML.find(keyword) == -1:
            return outer_HTML

def _parse_table_HTML(self, html:str)->dict:
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    rows = [i.strip() for i in text.split('\n') if not i.strip() == '']
    temp_course_list = [i for i in rows if not re.match(r'^\d\d\d\d\d', i.strip())==None]
    course_list = [[0 for y in range(3)] for x in range(len(courses))]
    for i in range(len(temp_course_list)):
        temp_course_list[i] = list(filter(None,temp_course_list[i].split(" ")))
        course_list[i] = temp_course_list[i][0:3]
    return {'title':rows[0], 'body':course_list}

def get_study_list(self):
    return self._get_table_HTML()


def _get_study_list_table_title(self, xpath="//table[0]/tbody/tr[1]/th/h2"):
    self._wait_until_present(By.XPATH, xpath)
    return self.driver.find_element_by_xpath(xpath).text
