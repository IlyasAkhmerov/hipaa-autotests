import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SecureEmailVerificationCode:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def get_message_subject(self):
        wait = WebDriverWait(self.driver, 10)
        subject = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-body .subject')))
        return subject.text

    def get_verification_code(self):
        wait = WebDriverWait(self.driver, 10)
        verification_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td div:nth-child(3) p strong')))
        return verification_code.text


