__author__ = 'sgulla'






class mortgage_calculator(object):
    def __init__(self,driver):
        self.driver=driver
    def set_home_price(self,price):
        self.driver.find_element_by_id("chouseprice").clear()
        self.driver.find_element_by_id("chouseprice").send_keys(price)
    def set_down_payment(self,payment):
        self.driver.find_element_by_id("cdownpayment").clear()
        self.driver.find_element_by_id("cdownpayment").send_keys(payment)




# class mortgagecalculator(object):
#     def __init__(self, driver):
#       self.driver = driver
#
#     def home_price(self, price):
#
#         self.driver.find_element_by_id("chouseprice").clear()
#         self.driver.find_element_by_id('chouseprice').send_key(price)
#
#
#
#
#     def downpayment(self, downpayment_value):
#         self.driver.find_element_by_id('cdownpayment').clear()
#         self.driver.find_element_by_id('cdownpayment').send_keys(downpayment_value)
#
