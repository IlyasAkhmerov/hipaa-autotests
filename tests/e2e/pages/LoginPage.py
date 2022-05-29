import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver

    def get_logo(self):
        wait = WebDriverWait(self.driver, 10)
        truvisibilityLogo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar.navbar-logo a span:nth-child(2)')))
        secureEmail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar.navbar-logo a span:nth-child(3)')))

        return truvisibilityLogo.text + ' ' + secureEmail.text

    def get_step_name(self):
        wait = WebDriverWait(self.driver, 10)
        stepName = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title span')))

        return stepName.text

    def get_StaySigned_checkbox(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form .checkbox-container')))

        return checkbox.text

    def get_help_link(self):
        wait = WebDriverWait(self.driver, 10)
        help_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(1)')))

        return help_link.text

    def click_help_link(self):
        wait = WebDriverWait(self.driver, 10)
        help_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(1)')))

        return help_link.click()

    def get_privacy_link(self):
        wait = WebDriverWait(self.driver, 10)
        privacy_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(2)')))

        return privacy_link.text

    def click_privacy_link(self):
        wait = WebDriverWait(self.driver, 10)
        privacy_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(2)')))

        return privacy_link.click()

    def get_terms_link(self):
        wait = WebDriverWait(self.driver, 10)
        terms_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(3)')))

        return terms_link.text

    def click_terms_link(self):
        wait = WebDriverWait(self.driver, 10)
        terms_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.service-container a:nth-child(3)')))

        return terms_link.click()

    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 20)
        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
        emailField.send_keys(email)
        nextButton = self.driver.find_element_by_css_selector('.btn.btn-primary')
        nextButton.click()
        time.sleep(2)

    def get_response_message(self):
        wait = WebDriverWait(self.driver, 10)
        response_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-container .error')))
        return response_message.text

    def clear_email_field(self):
        wait = WebDriverWait(self.driver, 10)
        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
        emailField.send_keys(Keys.CONTROL + "a")
        emailField.send_keys(Keys.DELETE)

