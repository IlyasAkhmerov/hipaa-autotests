import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class Header:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver

    def open_profile_menu(self):
        wait = WebDriverWait(self.driver, 10)
        profile_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.right-area .dropdown')))
        profile_menu.click()

    def get_profile_email(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area .dropdown .label-text-secondary')))
        time.sleep(0.5)
        profile_email = self.driver.find_element_by_css_selector('.right-area .dropdown .label-text-secondary')
        return profile_email.text

    def get_sign_out_item(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area .dropdown .label-text')))
        time.sleep(0.5)
        sign_out_item = self.driver.find_element_by_css_selector('.right-area .dropdown .label-text')
        return sign_out_item.text

    def click_sign_out_item(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area .dropdown .label-text')))
        time.sleep(0.5)
        sign_out_item = self.driver.find_element_by_css_selector('.right-area .dropdown .label-text')
        sign_out_item.click()



