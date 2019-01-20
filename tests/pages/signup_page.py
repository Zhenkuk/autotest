from selenium.webdriver.common.by import By

from tests.pages.locators import Locator


class SignUp(object):

    def __init__(self, driver):
        self.driver = driver

        #self.sign_up = driver.find_element(By.XPATH, Locator.sign_up)
        self.first_name = driver.find_element(By.XPATH, Locator.first_name)
        self.last_name = driver.find_element(By.XPATH, Locator.last_name)
        self.email = driver.find_element(By.XPATH, Locator.email)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.password_confirmation = driver.find_element(By.XPATH, Locator.password_confirmation)
        self.button_login = driver.find_element(By.XPATH, Locator.button_login)

    #def setSignUp(self):
        #self.check_this = sign_up
        #check_this.click()

    def setFirstName(self, Name):
        self.first_name.clear()
        self.first_name.send_keys(Name)

    def setLastName(self, Name):
        self.last_name.clear()
        self.last_name.send_keys(Name)

    def setEmail(self, email):
        self.email.clear()
        self.email.send_keys(email)

    def setPassword(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def setConfirmPassword(self, confirmPassword):
        self.password_confirmation.clear()
        self.password_confirmation.send_keys(confirmPassword)

    def submitRegistration(self):
        self.button_login.click()