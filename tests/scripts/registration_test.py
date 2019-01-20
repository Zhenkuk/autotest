import unittest
from time import sleep
from tests.pages.home_page import Home
from tests.pages.signup_page import SignUp
from tests.TestBase.environment_set_up import EnvironmentSetup



class Registration(EnvironmentSetup):

    def test_RegistrationFlow(self):

        driver = self.driver
        self.driver.get("https://locations.film")
        self.driver.set_page_load_timeout(20)


        home = Home(driver)
        if home.get_sign_up_text().is_displayed():
            print("Sign Up Link displaying")
            home.get_sign_up().click()
            sleep(4)


        reg = Register(driver)
        if reg.sign_up_text().is_displayed():
            print(reg.regis_txt.text)
        else:
            print("Registration page not loaded")
        try:
            reg.setFirstName("Zhenya")
            reg.setLastName("Kuk")
            reg.setEmail("Zhenya@gmail.com")
            reg.setPassword(12345678)
            reg.setConfirmPassword(12345678)


        post = Confirmation(driver)
        print(post.thankYou.text)
        if (post.UserID.text).find("Zhenya@gmail.com"):
            #print("Registration Process Successful")
        else:
            print("User Failed to register properly")



if __name__ == '__main__':
    unittest.main()