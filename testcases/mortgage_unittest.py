__author__ = 'sgulla'


__author__ = 'sgulla'

import unittest
import json, time

from selenium import webdriver
from pages.mortgage import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Loan_calculation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.calculator.net/mortgage-calculator.html"

    def test_calculate(self):
        driver = self.driver
        driver.get(self.base_url)
        mortgage = mortgage_calculator(driver)
        with open("mortgagedata") as data_file:
            data = json.load(data_file)
        home_price = data["homeprice"]
        print(home_price)
        mortgage.set_home_price(home_price)



    def tearDown(self):
        pass
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
'''

1. change the number of year > read this number from json > multiple iteration
2. calculate
3. view schuedle
4. Anual table displays same number of year as given in step1

'''
