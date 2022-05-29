import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from tests.e2e.pages.LeftSidebar import LeftSidebar

class NewEmail:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver
        self.leftsidebar_page = LeftSidebar(self.driver)

    def get_window_title(self):
        wait = WebDriverWait(self.driver, 10)
        window_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header .dialog-title')))
        return window_title.text

    def get_new_email_popup_title(self):
        try:
            self.driver.find_element_by_css_selector('.header .dialog-title')
        except NoSuchElementException:
            return False
        return True

    def get_cross_icon(self):
        try:
            #wait = WebDriverWait(self.driver, 10)
            #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.header .dialog-close-button')))
            self.driver.find_element_by_css_selector('.dialog .header .dialog-close-button')
        except NoSuchElementException:
            return False
        return True

    def click_cross_icon(self):
        wait = WebDriverWait(self.driver, 10)
        cross_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dialog .header .dialog-close-button')))
        cross_icon.click()

    def click_dialog_cross_icon(self):
        wait = WebDriverWait(self.driver, 10)
        cross_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'app-attention-dialog .dialog .header .dialog-close-button')))
        cross_icon.click()

    def get_to_field(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'recipients')))
        except NoSuchElementException:
            return False
        return True

    def get_subject_field(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.subject-area input')))
        except NoSuchElementException:
            return False
        return True

    def get_paper_clip(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.footer .left-area-actions')))
        except NoSuchElementException:
            return False
        return True

    def get_encrypted_switch_placeholder(self):
        wait = WebDriverWait(self.driver, 10)
        encrypted_switch_placeholder = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .secure-switcher')))
        return encrypted_switch_placeholder.text

    def get_encrypted_switch_status(self):
        wait = WebDriverWait(self.driver, 10)
        encrypted_switch_placeholder = wait.until(EC.visibility_of_element_located((By.ID, 'secureSwitch')))
        encrypted_status = encrypted_switch_placeholder.get_attribute('value')
        return encrypted_status

    def get_cancel_button_name(self):
        wait = WebDriverWait(self.driver, 10)
        cancel_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .btn:nth-child(1).btn-default')))
        return cancel_button.text

    def get_cancel_button(self):
        try:
            self.driver.find_element_by_css_selector('.header .dialog-close-button')
        except NoSuchElementException:
            return False
        return True

    def click_cancel_button(self):
        wait = WebDriverWait(self.driver, 10)
        cancel_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .btn:nth-child(1).btn-default')))
        cancel_button.click()

    def get_send_button(self):
        wait = WebDriverWait(self.driver, 10)
        send_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .btn.btn-success')))
        return send_button.text

    def click_send_button(self):
        wait = WebDriverWait(self.driver, 10)
        send_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.right-area-actions .btn.btn-success')))
        send_button.click()

    def click_send_button_in_the_confirmation_popup(self):
        wait = WebDriverWait(self.driver, 10)
        send_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dialog .btn-primary')))
        send_button.click()

    def enter_recipients_email_in_to_field(self, toRecipient):
        wait = WebDriverWait(self.driver, 10)
        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'recipients')))
        emailField.send_keys(toRecipient)

    def get_cc_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'form:nth-child(1) a:nth-child(1) span')
        except NoSuchElementException:
            return False
        return True

    def click_cc_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form:nth-child(1) a:nth-child(1) span')))
        cc_button = self.driver.find_element(By.CSS_SELECTOR, 'form:nth-child(1) a:nth-child(1) span')
        cc_button.click()

    def enter_recipients_email_in_cc_field(self, ccRecipient):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form:nth-child(1) a:nth-child(1) span')))
        # cc_button = self.driver.find_element(By.CSS_SELECTOR, 'form:nth-child(1) a:nth-child(1) span')
        # cc_button.click()
        cc_field = self.driver.find_element_by_id('ccRecipients')
        cc_field.send_keys(ccRecipient)

    def enter_email_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        emailField = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.subject-area input')))
        emailField.send_keys(subject)

    def get_warning_message(self):
        wait = WebDriverWait(self.driver, 10)
        message = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dialog .dialog-text span')))
        return message.text

    def get_email_sent_notification(self):
        wait = WebDriverWait(self.driver, 10)
        message = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.notification-container .notification-text')))
        return message.text

    def get_error_sending_notification(self):
        wait = WebDriverWait(self.driver, 10)
        message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification-container .notification-text')))
        return message.text

    def send_email_with_subject(self, recepientsEmail, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        time.sleep(1)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_unsecure_email_with_subject(self, recepientsEmail, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        time.sleep(1)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        secure_switch = self.driver.find_element_by_id('secureSwitch')
        secure_switch.click()
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_unsecure_email_to_multiple_recipients_with_subject(self, recepientsEmail, secondrecipientEmail, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        to_field.send_keys(Keys.ENTER)
        to_field.send_keys(secondrecipientEmail)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        secure_switch = self.driver.find_element_by_id('secureSwitch')
        secure_switch.click()
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_secure_email_to_multiple_recipients_with_subject(self, recepientsEmail, secondrecipientEmail, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        to_field.send_keys(Keys.ENTER)
        to_field.send_keys(secondrecipientEmail)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_secure_email_with_single_cc_recipient_and_subject(self, recepientsEmail, ccrecepient, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        cc_button = self.driver.find_element_by_css_selector('form:nth-child(1) a:nth-child(1) span')
        cc_button.click()
        cc_field = self.driver.find_element_by_id('ccRecipients')
        cc_field.send_keys(ccrecepient)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_secure_email_with_multiple_cc_recipient_and_subject(self, recepientsEmail, firstCCrecepient, secondCCrecepient, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        cc_button = self.driver.find_element_by_css_selector('form:nth-child(1) a:nth-child(1) span')
        cc_button.click()
        cc_field = self.driver.find_element_by_id('ccRecipients')
        cc_field.send_keys(firstCCrecepient)
        cc_field.send_keys(Keys.ENTER)
        cc_field.send_keys(secondCCrecepient)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_unsecure_email_with_multiple_cc_recipient_and_subject(self, recepientsEmail, firstCCrecepient, secondCCrecepient, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        cc_button = self.driver.find_element_by_css_selector('form:nth-child(1) a:nth-child(1) span')
        cc_button.click()
        cc_field = self.driver.find_element_by_id('ccRecipients')
        cc_field.send_keys(firstCCrecepient)
        cc_field.send_keys(Keys.ENTER)
        cc_field.send_keys(secondCCrecepient)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        secure_switch = self.driver.find_element_by_id('secureSwitch')
        secure_switch.click()
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_unsecure_email_with_cc_and_subject(self, recepientsEmail, ccrecepient, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        cc_button = self.driver.find_element_by_css_selector('form:nth-child(1) a:nth-child(1) span')
        cc_button.click()
        cc_field = self.driver.find_element_by_id('ccRecipients')
        cc_field.send_keys(ccrecepient)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        secure_switch = self.driver.find_element_by_id('secureSwitch')
        secure_switch.click()
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()

    def send_secure_email_with_single_bcc_recipient_and_subject(self, recepientsEmail, bccrecepient, messageSubject):
        to_field = self.driver.find_element_by_id('recipients')
        to_field.send_keys(recepientsEmail)
        bcc_button = self.driver.find_element_by_css_selector('form:nth-child(1) a:nth-child(2) span')
        bcc_button.click()
        bcc_field = self.driver.find_element_by_id('bccRecipients')
        bcc_field.send_keys(bccrecepient)
        subject_field = self.driver.find_element_by_css_selector('.subject-area input')
        subject_field.send_keys(messageSubject)
        send_button = self.driver.find_element_by_css_selector('.right-area-actions .btn.btn-success')
        send_button.click()