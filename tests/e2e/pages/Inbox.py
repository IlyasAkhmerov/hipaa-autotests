import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class Inbox:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver

    def get_incoming_message_status(self):
        wait = WebDriverWait(self.driver, 10)
        incomming_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.from-column span')))
        incomming_message_status = incomming_message.get_attribute('class')
        return incomming_message_status

    def get_status_of_incoming_message_with_number(self, messageNumber):
        wait = WebDriverWait(self.driver, 20)
        incomming_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'tr:nth-child(' + messageNumber + ') .from-column span')))
        incomming_message_status = incomming_message.get_attribute('class')
        return incomming_message_status

    def open_message_with_number(self, messageNumber):
        wait = WebDriverWait(self.driver, 20)
        message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'tr:nth-child(' + messageNumber + ') .from-column')))
        message.click()

    def clear_inbox(self):
        wait = WebDriverWait(self.driver, 10)
        mass_action_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.page-actions .rounded-checkbox-container')))
        mass_action_checkbox.click()
        delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a:nth-child(6)')))
        delete_button.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.empty-folder .empty-folder-text')))


