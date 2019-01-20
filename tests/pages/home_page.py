from selenium.webdriver.common.by import By

from tests.pages.locators import Locator


class Home(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.sign_up_text = driver.find_element(By.XPATH, Locator.sign_up_text)
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.my_cart = driver.find_element(By.XPATH, Locator.my_cart)
        self.sign_up = driver.find_element(By.XPATH, Locator.sign_up)
        self.login = driver.find_element(By.XPATH, Locator.login)
        self.logout = driver.find_element(By.XPATH, Locator.logout)
        self.account = driver.find_element(By.XPATH, Locator.account)
        self.favorites = driver.find_element(By.XPATH, Locator.favorites)

    def get_sign_up_text(self):
        return self.sign_up_text

    def get_logo(self):
        return self.logo

    def get_my_cart(self):
        return self.my_cart

    def get_sign_up(self):
        return self.sign_up

    def get_login(self):
        return self.login

    def get_logout(self):
        return self.logout

    def get_account(self):
        return self.account

    def get_favorites(self):
        return self.favorites
