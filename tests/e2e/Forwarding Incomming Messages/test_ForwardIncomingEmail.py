import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from qaseio.pytest import qase
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.PasswordRecoveryPage import PasswordRecoveryPage
from tests.e2e.pages.LeftSidebar import LeftSidebar
from tests.e2e.pages.ListOfEmailsPage import ListOfEmails
from tests.e2e.pages.NewEmailPage import NewEmail
from tests.e2e.pages.ViewEmailPage import ViewEmail
from selenium.webdriver.common.keys import Keys



# _________________________________________________________________________________
# В тесте проверяются кейсы, связанные с пересылкой входящих писем
# _________________________________________________________________________________

class ForwardIncommingEmailsTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()
        email = config.secure_email
        password = config.password

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.password_recovery_page = PasswordRecoveryPage(self.driver)
        self.leftsidebar_page = LeftSidebar(self.driver)
        self.new_email_page = NewEmail(self.driver)
        self.list_of_emails_page = ListOfEmails(self.driver)
        self.view_email_page = ViewEmail(self.driver)


        self.password_page.authorization(email=email, password=password)
        self.leftsidebar_page.click_new_email_button()

    def tearDown(self) -> None:
        self.view_email_page.click_delete_button()
        self.list_of_emails_page.get_list_of_emails()
        self.driver.quit()

        super().tearDown()


    qase.id(311)
    def test_ForwardEmail_ForwardSecureEmailsFromUnsecuredAccount_EncryptedSwitchOnAndDisabled(self):
        config = ConfigManager.get_config()
        recipients_email = config.alternative_email_for_secure
        password = config.password
        self.new_email_page.send_email_with_subject(recipients_email, 'Secure message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Secure message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('true', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual('true', status)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_secure_email_from_unsecure_account.png')


    @qase.id(312)
    def test_ForwardEmail_ForwardUnsecureEmailsFromUnsecuredAccount_EncryptedSwitchOffAndDisabled(self):
        config = ConfigManager.get_config()
        recipients_email = config.alternative_email_for_secure
        password = config.password
        self.new_email_page.send_unsecure_email_with_subject(recipients_email, 'Unprotected message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Unprotected message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Unprotected message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Unprotected message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('false', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual('true', status)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_unsecure_email_from_unsecure_account.png')

    @qase.id(313)
    def test_ForwardEmail_ForwardSecureEmailsFromSecureAccount_EncryptedSwitchOnAndNotDisabled(self):
        config = ConfigManager.get_config()
        recipients_email = config.secure_email_second
        password = config.password_second
        self.new_email_page.send_email_with_subject(recipients_email, 'Secure message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Secure message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('true', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual('true', status)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_secure_email_from_secure_account.png')

    @qase.id(314)
    def test_ForwardEmail_ForwardUnsecureEmailsFromSecureAccount_EncryptedSwitchOffAndNotDisabled(self):
        config = ConfigManager.get_config()
        recipients_email = config.secure_email_second
        password = config.password_second
        self.new_email_page.send_unsecure_email_with_subject(recipients_email, 'Unprotected message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Unprotected message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Unprotected message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Unprotected message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('false', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual(None, status)
        self.view_email_page.enter_recipients_email_in_to_field('email@example.com')
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('false', encrypted_switch_status)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_unsecure_email_from_secure_account.png')

    @qase.id(308)
    def test_ForwardEmail_ForwardEmailsWithoutRecipients_NotificationPopupAppears(self):
        config = ConfigManager.get_config()
        recipients_email = config.alternative_email_for_secure
        password = config.password
        self.new_email_page.send_email_with_subject(recipients_email, 'Secure message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Secure message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('true', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual('true', status)
        self.view_email_page.click_send_button()
        self.view_email_page.get_error_popup()
        error_message = self.view_email_page.get_error_message()
        self.assertEqual('Message not sent. Please, try again later.', error_message)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_without_recipient_error_popup.png')
        self.view_email_page.click_cross_icon()

    @qase.id(306)
    def test_ForwardEmail_Shortcut_Success(self):
        config = ConfigManager.get_config()
        recipients_email = config.alternative_email_for_secure
        password = config.password
        self.new_email_page.send_email_with_subject(recipients_email, 'Secure message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Secure message to forward')
        body_tab = self.driver.find_element(By.TAG_NAME, "body")
        body_tab.send_keys('f')
        forward_window_title = self.view_email_page.get_window_title()
        self.assertEqual('Forward', forward_window_title)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/forward_secure_email_shortcut.png')

    @qase.id(315)
    def test_ForwardEmail_ForwardSecureEmailsFromUnsecuredAccount_SuccessfulSending(self):
        config = ConfigManager.get_config()
        recipients_email = config.alternative_email_for_secure
        password = config.password
        self.new_email_page.send_email_with_subject(recipients_email, 'Secure message to forward')

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.driver.get(config.staging_url)
        self.password_page.authorization(recipients_email, password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Secure message to forward')
            attempt += 1
        self.list_of_emails_page.open_message_with_subject('Secure message to forward')
        self.view_email_page.get_forward_button()
        self.view_email_page.click_forward_button()
        encrypted_switch_status = self.view_email_page.get_encrypted_switch_status()
        self.assertEqual('true', encrypted_switch_status)
        status = self.view_email_page.get_encrypted_switch_disabled_status()
        self.assertEqual('true', status)
        self.view_email_page.enter_recipients_email_in_to_field('email@example.ru')
        self.view_email_page.click_send_button()

        window = self.driver.window_handles[0]
        self.driver.switch_to.window(window)
        self.driver.get(config.staging_url)
        self.password_page.authorization('email@example.ru', password=password)

        self.list_of_emails_page.get_list_of_emails()
        email = self.list_of_emails_page.get_message_with_subject('Fwd: Secure message to forward')
        attempt = 1
        while email == False and attempt <= 7:
            self.list_of_emails_page.click_refresh_icon()
            time.sleep(1)
            email = self.list_of_emails_page.get_message_with_subject('Fwd: Secure message to forward')
            attempt += 1

        self.list_of_emails_page.open_message_with_subject('Fwd: Secure message to forward')
        message_subject = self.view_email_page.get_message_subject()
        self.assertEqual('Fwd: Secure message to forward', message_subject)
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot('/HIPAA_Auto_Tests/screenshots/message_to_forward/viewing_received_forwarded_message.png')

    #
    #
    #


