import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class SearchPage:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def get_search_bar(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-bar input')))
            self.driver.find_element_by_css_selector('.search-bar input')
        except NoSuchElementException:
            return False
        return True

    def clear_search_bar(self):
        search_bar = self.driver.find_element_by_css_selector('.search-bar input')
        search_bar.clear()

    def get_loup_icon(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.search-bar a:nth-child(1)')))
            self.driver.find_element_by_css_selector('div.search-bar a:nth-child(1)')
        except NoSuchElementException:
            return False
        return True

    def click_loup_icon(self):
        loup_icon = self.driver.find_element_by_css_selector('div.search-bar a:nth-child(1)')
        loup_icon.click()

    def hover_over_loup_icon(self):
        wait = WebDriverWait(self.driver, 10)
        loup_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search-bar a:nth-child(1)')))
        ActionChains(self.driver).move_to_element(loup_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_placeholder(self):
        wait = WebDriverWait(self.driver, 10)
        search_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-bar input')))
        placeholder = search_bar.get_attribute('placeholder')
        return placeholder

    def enter_a_search_query_in_the_search_bar(self, query):
        wait = WebDriverWait(self.driver, 10)
        search_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-bar input')))
        search_bar.send_keys(query)

    def enter_a_search_query_in_the_from_field(self, query):
        wait = WebDriverWait(self.driver, 10)
        from_field = wait.until(EC.presence_of_element_located((By.ID, 'from')))
        from_field.send_keys(query)

    def get_clear_search_icon(self):
        try:
            self.driver.find_element_by_css_selector('[mattooltip="Clear search"]')
        except NoSuchElementException:
            return False
        return True

    def click_clear_search_icon(self):
        clear_search_icon = self.driver.find_element_by_css_selector('[mattooltip="Clear search"]')
        clear_search_icon.click()

    def get_search_filter_icon(self):
        try:
            self.driver.find_element_by_id('filter-button')
        except NoSuchElementException:
            return False
        return True

    def hover_search_filter_icon(self):
        wait = WebDriverWait(self.driver, 10)
        search_filter_icon = wait.until(EC.presence_of_element_located((By.ID, 'filter-button')))
        ActionChains(self.driver).move_to_element(search_filter_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_search_filter_icon(self):
        wait = WebDriverWait(self.driver, 10)
        search_filter_icon = wait.until(EC.element_to_be_clickable((By.ID, 'filter-button')))
        search_filter_icon.click()

    def get_from_field_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id('from')
        except NoSuchElementException:
            return False
        return placeholder.get_attribute('placeholder')

    def get_to_field_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id('to')
        except NoSuchElementException:
            return False
        return placeholder.get_attribute('placeholder')

    def get_subject_field_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id('subject')
        except NoSuchElementException:
            return False
        return placeholder.get_attribute('placeholder')

    def get_hasword_field_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id('hasWords')
        except NoSuchElementException:
            return False
        return placeholder.get_attribute('placeholder')

    def get_doesnothave_field_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id('notWords')
        except NoSuchElementException:
            return False
        return placeholder.get_attribute('placeholder')

    def get_datewithin_field(self):
        try:
            datewithin_field = self.driver.find_element_by_css_selector('div:nth-child(7) .label-wrapper label')
        except NoSuchElementException:
            return False
        return datewithin_field.text

    def open_datewithin_dropdown(self):
        datewithin_dropdown = self.driver.find_element_by_css_selector('div:nth-child(7).field-wrapper .dropdown .dropdown-toggle')
        datewithin_dropdown.click()

    def get_search_field(self):
        try:
            search_field = self.driver.find_element_by_css_selector('div:nth-child(8) .label-wrapper label')
        except NoSuchElementException:
            return False
        return search_field.text

    def open_search_dropdown(self):
        search_field = self.driver.find_element_by_css_selector('div:nth-child(8).field-wrapper .dropdown .dropdown-toggle')
        search_field.click()

    def get_search_button(self):
        try:
            search_button = self.driver.find_element_by_css_selector('.footer .btn')
        except NoSuchElementException:
            return False
        return search_button.text

    def get_empty_search_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.empty-search span:nth-child(2)')))
        message = self.driver.find_element_by_css_selector('.empty-search span:nth-child(2)')
        return message.text

    def click_search_button(self):
        wait = WebDriverWait(self.driver, 10)
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.footer .btn')))
        search_button.click()

    def get_invalid_search_query_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification-container .notification-text')))
        message = self.driver.find_element_by_css_selector('.notification-container .notification-text')
        return message.text


