import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SecurityAlertPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def get_message_subject(self):
        wait = WebDriverWait(self.driver, 10)
        subject = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-body .subject')))
        return subject.text

    def get_info_message(self):
        wait = WebDriverWait(self.driver, 10)
        message_body = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#content .message-text tbody tr:nth-child(2) td div div:nth-child(2) div')))
        return message_body


    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url



