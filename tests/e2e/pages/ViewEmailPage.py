import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


class ViewEmail:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver

    def back_arrow_hover_over(self):
        wait = WebDriverWait(self.driver, 10)
        back_arrow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.left-actions-area a:nth-child(1)')))
        ActionChains(self.driver).move_to_element(back_arrow).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_back_arrow(self):
        try:
            self.driver.find_element_by_css_selector('.left-actions-area a:nth-child(1)')
        except NoSuchElementException:
            return False

    def click_back_arrow(self):
        wait = WebDriverWait(self.driver, 10)
        back_arrow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.left-actions-area a:nth-child(1)')))
        back_arrow.click()

    def starred_icon_hover_over(self):
        wait = WebDriverWait(self.driver, 10)
        starred_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.left-actions-area a:nth-child(2)')))
        ActionChains(self.driver).move_to_element(starred_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_starred_value_of_emails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.left-actions-area a:nth-child(2)')))
        starred_status = self.driver.find_element_by_css_selector('.left-actions-area a:nth-child(2)')
        starred_value = starred_status.get_attribute('aria-describedby')
        return starred_value

    def get_starred_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        star_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.left-actions-area a:nth-child(2)')))
        ActionChains(self.driver).move_to_element(star_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_starred_icon(self):
        wait = WebDriverWait(self.driver, 10)
        starred_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.left-actions-area a:nth-child(2)')))
        starred_icon.click()

    def click_mark_as_unread_icon(self):
        wait = WebDriverWait(self.driver, 10)
        mark_as_unread_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Mark As Unread"]')))
        mark_as_unread_icon.click()

    def get_mark_as_unread_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        envelope_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Mark As Unread"]')))
        ActionChains(self.driver).move_to_element(envelope_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_delete_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        envelope_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Delete"]')))
        ActionChains(self.driver).move_to_element(envelope_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_reply_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        reply_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.right-actions-area a[mattooltip="Reply"]')))
        ActionChains(self.driver).move_to_element(reply_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_forward_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        envelope_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a:nth-child(2)[mattooltip="Forward"]')))
        ActionChains(self.driver).move_to_element(envelope_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_replyall_button(self):
        try:
            reply_all_btn = self.driver.find_element_by_css_selector('.actions-container div button:nth-child(2) span')
            return reply_all_btn.text
        except NoSuchElementException:
            return False

    def click_replyall_button(self):
        wait = WebDriverWait(self.driver, 10)
        replyall_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.actions-container div button:nth-child(2) span')))
        replyall_button.click()

    def get_reply_icon(self):
        try:
            self.driver.find_element_by_css_selector('a:nth-child(1)[mattooltip="Reply"]')
            return True
        except NoSuchElementException:
            return False

    def click_reply_icon(self):
        wait = WebDriverWait(self.driver, 10)
        reply_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a:nth-child(1)[mattooltip="Reply"]')))
        reply_icon.click()

    def get_reply_button(self):
        try:
            reply_btn = self.driver.find_element_by_css_selector('.actions-container div button:nth-child(1) span')
            return reply_btn.text
        except NoSuchElementException:
            return False

    def click_reply_button(self):
        wait = WebDriverWait(self.driver, 10)
        reply_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.actions-container div button:nth-child(1) span')))
        reply_button.click()

    def get_replyall_icon(self):
        try:
            reply_all_icon = self.driver.find_element_by_css_selector('a:nth-child(2)[mattooltip="Reply All"]')
            return reply_all_icon.text
        except NoSuchElementException:
            return False

    def click_replyall_icon(self):
        wait = WebDriverWait(self.driver, 10)
        replyall_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a:nth-child(2)[mattooltip="Reply All"]')))
        replyall_icon.click()

    def get_forward_button(self):
        try:
            self.driver.find_element_by_css_selector('.actions-container div button:nth-child(2) span')
        except NoSuchElementException:
            return False

    def click_forward_button(self):
        wait = WebDriverWait(self.driver, 10)
        forward_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.actions-container div button:nth-child(2) span')))
        forward_button.click()

    def click_delete_button(self):
        wait = WebDriverWait(self.driver, 10)
        delete_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Delete"]')))
        delete_icon.click()

    def get_encrypted_switch_status(self):
        wait = WebDriverWait(self.driver, 10)
        encrypted_switch = wait.until(EC.visibility_of_element_located((By.ID, 'secureSwitch')))
        encrypted_switch_status = encrypted_switch.get_attribute('value')
        return encrypted_switch_status

    def get_encrypted_switch_disabled_status(self):
        wait = WebDriverWait(self.driver, 10)
        encrypted_switch = wait.until(EC.visibility_of_element_located((By.ID, 'secureSwitch')))
        encrypted_switch_disabled_status = encrypted_switch.get_attribute('disabled')
        return encrypted_switch_disabled_status

    def clear_recipients_field(self):
        wait = WebDriverWait(self.driver, 10)
        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'recipients')))
        emailField.send_keys(Keys.CONTROL + 'A')
        emailField.send_keys(Keys.DELETE)

    def enter_recipients_email_in_to_field(self, recipient):
        wait = WebDriverWait(self.driver, 10)
        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'recipients')))
        emailField.send_keys(recipient)

    def click_send_button(self):
        wait = WebDriverWait(self.driver, 10)
        send_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .btn.btn-success')))
        send_button.click()

    def get_error_popup(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'mat-dialog-container .dialog')))
        except NoSuchElementException:
            return False

    def get_error_message(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'mat-dialog-container .dialog span')))
            return error_message.text
        except NoSuchElementException:
            return False

    def click_cross_icon(self):
        wait = WebDriverWait(self.driver, 10)
        cross_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dialog .header .dialog-close-button')))
        cross_icon.click()

    def get_window_title(self):
        wait = WebDriverWait(self.driver, 10)
        window_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.message-editor .header span')))
        return window_title.text

    def get_message_subject(self):
        wait = WebDriverWait(self.driver, 10)
        message_subject = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-body .subject span')))
        return message_subject.text

    def save_screenshot(self, name):
        path = '/HIPAA_Auto_Tests/screenshots/view_email/'
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        self.driver.save_screenshot(path + name)

    def get_unwrap_icon(self):
        try:
            self.driver.find_element_by_css_selector('button[mattooltip="Show trimmed content"]')
            return True
        except NoSuchElementException:
            return False

    def get_unwrap_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        unwrap_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[mattooltip="Show trimmed content"]')))
        ActionChains(self.driver).move_to_element(unwrap_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text





