__author__ = 'sgulla'

from selenium import webdriver
class mortgage_calculator(object):
    def __init__(self,driver):
        self.driver=driver
    def set_home_price(self,price):
        self.driver.find_element_by_id("chouseprice").clear()
        self.driver.find_element_by_id("chouseprice").send_keys()
