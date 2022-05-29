import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SupportPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def get_page_title(self):
        wait = WebDriverWait(self.driver, 10)
        page_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.widget:nth-child(1) .text-container h3 span')))
        return page_title.text

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

