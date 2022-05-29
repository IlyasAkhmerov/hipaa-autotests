import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class PasswordRecoveryPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def click_forgot_password_link(self):
        wait = WebDriverWait(self.driver, 20)
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.forgot-password')))
        forgot_password_link.click()
        time.sleep(5)

    def get_step_name(self):
        wait = WebDriverWait(self.driver, 10)
        step_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title span')))
        return step_name.text

    def get_email(self):
        wait = WebDriverWait(self.driver, 10)
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sub-title-email span')))

        return email.text

    def get_information_message(self):
        wait = WebDriverWait(self.driver, 10)
        info_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.sub-title span')))
        return info_message.text

    def get_message_about_sending_code(self):
        wait = WebDriverWait(self.driver, 10)
        info_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.after-email-content span')))
        return info_message.text

    def get_hidden_email(self):
        config = ConfigManager.get_config()
        alternative_email = config.alternative_email_for_secure.split('@')
        name = str(alternative_email[0])
        domain_part = alternative_email[1].split(('.'))
        subdomain = str(domain_part[0])
        domain = str(domain_part[1])
        new_name = str(name[0] + '*' * (len(name) - 2) + name[-1])
        new_subdomain = str('*' * (len(subdomain) - 2) + subdomain[-1])
        secret_email = str(new_name + '@' + new_subdomain + '.' + domain)
        return secret_email

    def get_placeholder(self):
        wait = WebDriverWait(self.driver, 10)
        codeInputfield = wait.until(EC.visibility_of_element_located((By.ID, 'recoveryCode')))
        placeholder = codeInputfield.get_attribute('placeholder')
        return placeholder

    def get_note(self):
        wait = WebDriverWait(self.driver, 10)
        note = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.note span')))
        return note.text

    def get_SendAgain_message(self):
        wait = WebDriverWait(self.driver, 10)
        message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.send-again span')))
        return message.text

    def get_SendAgain_link(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.send-again a')))
        return link.text

    def get_SignIn_button(self):
        wait = WebDriverWait(self.driver, 10)
        sign_in_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-primary ')))
        return sign_in_button.text

    def click_SignIn_button(self):
        wait = WebDriverWait(self.driver, 10)
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary ')))
        sign_in_button.click()

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 20)
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
        next_button.click()

    def get_response_message(self):
        wait = WebDriverWait(self.driver, 10)
        response_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-container .error span')))
        return response_message.text

    def enter_wrong_code(self, wrong_code):
        wait = WebDriverWait(self.driver, 10)
        codeField = wait.until(EC.element_to_be_clickable((By.ID, 'recoveryCode')))
        codeField.send_keys(wrong_code)

    def enter_new_password(self, new_password):
        wait = WebDriverWait(self.driver, 20)
        passwordField = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
        passwordField.send_keys(new_password)

    def confirm_new_password(self, new_password):
        wait = WebDriverWait(self.driver, 20)
        confirm_password_field = wait.until(EC.element_to_be_clickable((By.ID, 'confirmPassword')))
        confirm_password_field.send_keys(new_password)

        submitButton = self.driver.find_element_by_css_selector('.btn.btn-primary')
        submitButton.click()









