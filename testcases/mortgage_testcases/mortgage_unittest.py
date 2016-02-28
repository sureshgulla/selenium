__author__ = 'sgulla'



import unittest
import json, time

import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
print(path)

from selenium import webdriver
from Configs.config_details import *

from pages.mortgage import *
class Loan_calculation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = url

    def test_calculate(self):

        driver = self.driver
        driver.get(self.base_url)

        mortgagepage = mortgage_calculator(driver)


        with open(path+"/data/mortgagedata.json") as data_file:
            data = json.load(data_file)
        home_price = data["homeprice"]
        print(home_price)
        mortgagepage.set_home_price(home_price)




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
