import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/eugene/first_test/drivers/chromedriver')
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
     if (self.driver != None):

        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()