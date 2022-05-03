from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "fm-login-id"
        self.password_textbox_id = "fm-login-password"
        self.login_button_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[3]/div/button'
        self.login_button_on_pop_up_xpath = '//*[@id="modal-popup-zh"]/div[2]/div/div[2]/div[3]/div/button'
        self.invalidPasswordEmail_message_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[3]/div/div[6]/span'
        self.reg_email_field_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[2]/input'
        self.reg_pass_field_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div[1]/input'
        self.reg_btn_xpath = '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div/div/button'
        self.change_email_btn_xpath = '/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/p[2]/span'

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_password_message(self):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        msg = self.driver.find_element(By.XPATH, self.invalidPasswordEmail_message_xpath).text
        return msg

    def check_invalid_login_message(self):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        msg = self.driver.find_element(By.XPATH, self.invalidPasswordEmail_message_xpath).text
        return msg

    def click_login_on_pop_up(self):
        self.driver.find_element(By.XPATH, self.login_button_on_pop_up_xpath).click()
        self.driver.implicitly_wait(10)

    def enter_reg_email(self, email):
        self.driver.find_element(By.XPATH, self.reg_email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.reg_email_field_xpath).send_keys(email)

    def enter_reg_password(self, password):
        self.driver.find_element(By.XPATH, self.reg_pass_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.reg_pass_field_xpath).send_keys(password)

    def click_enter_reg(self):
        self.driver.find_element(By.XPATH, self.reg_btn_xpath).click()

    def click_change_email_btn(self):
        self.driver.find_element(By.XPATH, self.change_email_btn_xpath).click()
