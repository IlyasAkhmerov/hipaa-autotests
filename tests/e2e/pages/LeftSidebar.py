import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class LeftSidebar:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver

    def get_inbox_folder(self):
        wait = WebDriverWait(self.driver, 60)
        inbox_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folder:nth-child(1) span')))

        return inbox_folder.text

    def get_inbox_folder_status(self):
        wait = WebDriverWait(self.driver, 10)
        inbox_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(1)')))
        inbox_folder_status = inbox_folder.get_attribute('class')

        return inbox_folder_status

    def go_to_inbox(self):
        wait = WebDriverWait(self.driver, 10)
        inbox_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(1)')))
        inbox_folder.click()

    def get_sent_folder(self):
        wait = WebDriverWait(self.driver, 10)
        sent_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folder:nth-child(2) span')))

        return sent_folder.text

    def get_sent_folder_status(self):
        wait = WebDriverWait(self.driver, 10)
        sent_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(2)')))
        sent_folder_status = sent_folder.get_attribute('class')

        return sent_folder_status

    def collapse_leftsidebar(self):
        wait = WebDriverWait(self.driver, 10)
        my_menu_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[mattooltip="Main menu"]')))

        my_menu_icon.click()

    def expand_leftsidebar(self):
        wait = WebDriverWait(self.driver, 10)
        my_menu_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[mattooltip="Main menu"]')))
        my_menu_icon.click()

    def get_leftsidebar_status(self):
        wait = WebDriverWait(self.driver, 10)
        leftsidebar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content app-sidebar section')))
        leftsidebar_status = leftsidebar.get_attribute('class')
        return leftsidebar_status

    def get_new_email_button(self):

        wait = WebDriverWait(self.driver, 10)
        new_email_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft button span:nth-child(2)')))
        return new_email_button.text

    def click_new_email_button(self):

        wait = WebDriverWait(self.driver, 10)
        new_email_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft button span:nth-child(2)')))
        new_email_button.click()

    def hover_over_menu_icon(self):
        wait = WebDriverWait(self.driver, 10)
        my_menu_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[mattooltip="Main menu"]')))
        ActionChains(self.driver).move_to_element(my_menu_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def hover_over_new_email_button(self):
        wait = WebDriverWait(self.driver, 10)
        new_email_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft.slim .btn.btn-success')))
        ActionChains(self.driver).move_to_element(new_email_button).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))

        return  tooltip.text

    def hover_over_inbox_folder(self):
        wait = WebDriverWait(self.driver, 10)
        inbox_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(1)')))
        ActionChains(self.driver).move_to_element(inbox_folder).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))

        return  tooltip.text

    def hover_over_sent_folder(self):
        wait = WebDriverWait(self.driver, 10)
        sent_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(2)')))
        ActionChains(self.driver).move_to_element(sent_folder).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))

        return  tooltip.text

    def click_sent_folder(self):
        wait = WebDriverWait(self.driver, 10)
        sent_folder = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sidebarleft .folders .folder:nth-child(2)')))

        sent_folder.click()
