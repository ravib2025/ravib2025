from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_id = "btnLogin"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLoinBtn(self):
        self.driver.find_element(By.ID, self.button_login_id)




