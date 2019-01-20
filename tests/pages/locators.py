class Locator(object):

    # Home Page locator  https://locations.film/

    logo = "//img[@class='tm-logo-sticky']"
    my_cart = "//ul[@class='uk-navbar-nav uk-hidden-small']//li[2]//a[1]"
    sign_up = "//ul[@class='uk-navbar-nav uk-hidden-small']//li[3]//a[1]"
    login = "//li[@id='tm-button-login']//a"
    logout = "//a[contains(text(),'Logout')]"
    account = "//a[contains(text(),'Account')]"
    favorites = "//a[contains(text(),'Favorites')]"

    # Sign Up Page locator   https://locations.film/sign-up

    sign_up_text = "//h3[@class='padV15 text-center']"
    first_name = "//input[@id='first_name']"
    last_name = "//input[@id='last_name']"
    email = "//input[@id='email']"
    password = "//input[@id='password']"
    password_confirmation = "//div[5]/input"
    button_login = "//section[@id='main']/div/div/div/div/form/div[6]/button/b"

    # Login Page locator   https://locations.film/log-in

    login_email = "//section[@id='main']/div/div/div/div/form/div/div/input"
    login_password = "//input[@id='password']"
    login_button_login = "//section[@id='main']/div/div/div/div/form/div[3]/button/b"

    # Account Page locator

    account_details = "//h3[contains(text(),'Account Details')]"
    update_details_password = "//div[@class='padVt10']//a[1]"
    credit_card = "//div[@class='padVt10']//a[2]"
    billing = "//div[@class='padVt10']//a[3]"

    # Post registration locator

    welcome_message = "//*[contains(text(),'Welcome to Easy Locations')]"
