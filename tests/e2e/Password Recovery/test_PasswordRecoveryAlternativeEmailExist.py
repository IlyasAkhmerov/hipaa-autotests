import unittest
from qaseio.pytest import qase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.PasswordRecoveryPage import PasswordRecoveryPage
from tests.e2e.pages.SecureEmailVerificationCodePage import SecureEmailVerificationCode
from tests.e2e.pages.SecurityAlertsPage import SecurityAlertPage
from tests.e2e.pages.Inbox import Inbox
from tests.e2e.pages.ListOfEmailsPage import ListOfEmails
from selenium.webdriver.common.keys import Keys

from tests.e2e.pages.LeftSidebar import LeftSidebar

# _________________________________________________________________________________
# В тесте проверяются кейсы восстановления пароля
# _________________________________________________________________________________

class PasswordRecoveryTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()
        registered_email = config.secure_email

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.password_recovery_page = PasswordRecoveryPage(self.driver)
        self.leftsidebar_page = LeftSidebar(self.driver)
        self.secure_email_verification_code = SecureEmailVerificationCode(self.driver)
        self.inbox_page = Inbox(self.driver)
        self.security_alert_page = SecurityAlertPage(self.driver)
        self.list_of_emails_page = ListOfEmails(self.driver)


        self.login_page.enter_email(registered_email)
        self.password_recovery_page.click_forgot_password_link()

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()



    @qase.id(22, 132)
    def test_PasswordRecovery_ClickByForgotPasswordLink_ResetPasswordScreenOpens(self):

        title = self.password_recovery_page.get_step_name()
        self.assertEqual('Reset Password', title)

    @qase.id(22, 132)
    def test_PasswordRecovery_ResetPasswordScreen_TitleIsPresent(self):

        step_name = self.password_recovery_page.get_step_name()
        self.assertEqual('Reset Password', step_name)

    @qase.id(22, 132)
    def test_PasswordRecovery_ResetPasswordScreen_EmailIsPresent(self):

        email = self.password_recovery_page.get_email()
        config = ConfigManager.get_config()
        login = config.secure_email
        self.assertEqual(login, email)

    @qase.id(132)
    def test_PasswordRecovery_ResetPasswordScreenValidPassword_InfoMessageIsPresent(self):

        info_message = self.password_recovery_page.get_message_about_sending_code()
        hidden_email = self.password_recovery_page.get_hidden_email()
        self.assertEqual('Please type in the verification code that was just emailed to ' + hidden_email + '.', info_message)

    @qase.id(132)
    def test_PasswordRecovery_ResetPasswordScreenValidPassword_PlaceholderPresent(self):

        placeholder = self.password_recovery_page.get_placeholder()
        self.assertEqual('Verification code', placeholder)

    @qase.id(132)
    def test_PasswordRecovery_ResetPasswordScreenValidPassword_NoteIsPresent(self):

        note = self.password_recovery_page.get_note()
        self.assertEqual('* Please check spam/promo folders for email.', note)

    @qase.id(132)
    def test_PasswordRecovery_ResetPasswordScreenValidPassword_SendAgainMessageIsPresent(self):

        send_again_message = self.password_recovery_page.get_SendAgain_message()
        self.assertEqual("Don't see the email?", send_again_message)

    @qase.id(132)
    def test_PasswordRecovery_ResetPasswordScreenValidPassword_SendAgainLinkIsPresent(self):

        send_again_link = self.password_recovery_page.get_SendAgain_link()
        self.assertEqual("Send a new email.", send_again_link)

    @qase.id(132)
    def test_PasswordRecovery_EmptyCodeField_ErrorMessage(self):

        self.password_recovery_page.click_next_button()
        error_message = self.password_recovery_page.get_response_message()
        self.assertEqual('Verification code is incorrect', error_message)

    @qase.id(132)
    def test_PasswordRecovery_WrongCode_ErrorMessage(self):

        self.password_recovery_page.click_next_button()
        self.password_recovery_page.enter_wrong_code('VLEJ81')
        error_message = self.password_recovery_page.get_response_message()
        self.assertEqual('Verification code is incorrect', error_message)


    @qase.id(20)
    def test_PasswordRecovery_ValidCode_Success(self):

        config = ConfigManager.get_config()
        email = config.secure_email
        password = config.password
        alternative_for_secure_email = config.alternative_email_for_secure

        self.password_recovery_page.click_next_button()

        self.driver.execute_script("window.open();")
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        config = ConfigManager.get_config()
        self.driver.get(config.staging_url)

        self.login_page.clear_email_field()
        self.login_page.enter_email(alternative_for_secure_email)
        self.password_page.enter_password(password)
        self.password_page.click_next_button()

        inbox_folder = self.leftsidebar_page.get_inbox_folder()
        self.assertEqual('Inbox', inbox_folder)
        inbox_folder_status = self.leftsidebar_page.get_inbox_folder_status()
        self.assertEqual('folder active', inbox_folder_status)
        incomming_message_status = self.inbox_page.get_status_of_incoming_message_with_number('1')
        self.assertEqual('unread', incomming_message_status)

        self.list_of_emails_page.open_message_with_subject('TruVISIBILITY Secure Email reset password')

        message_subject = self.secure_email_verification_code.get_message_subject()
        self.assertEqual('TruVISIBILITY Secure Email reset password', message_subject)

        self.driver.save_screenshot('E:\HIPAA_Auto_Tests\screenshots\security_alerts\security_message_with_verification_code.png')

        verification_code = self.secure_email_verification_code.get_verification_code()

        previous_window = self.driver.window_handles[0]
        self.driver.switch_to.window(previous_window)

        codeField = self.driver.find_element(By.ID, 'recoveryCode')
        codeField.send_keys(verification_code)

        self.password_recovery_page.click_next_button()

        self.password_recovery_page.enter_new_password(password)
        self.password_recovery_page.confirm_new_password(password)
        time.sleep(2)

        step_name = self.password_recovery_page.get_step_name()
        self.assertEqual('Password changed', step_name)

        info_message = self.password_recovery_page.get_information_message()
        self.assertEqual('You have successfully changed your password', info_message)

        self.password_recovery_page.click_SignIn_button()
        self.login_page.enter_email(email)
        self.password_page.enter_password(password)
        self.password_page.click_next_button()

        inbox_folder = self.leftsidebar_page.get_inbox_folder()
        self.assertEqual('Inbox', inbox_folder)

        self.inbox_page.open_message_with_number('2')

        info_message = self.security_alert_page.get_info_message()
        self.assertEqual('Your password was changed', info_message.text)

    '''Перемещение по элементам с помощью клавиш Tab и Shif+Tab'''

    @qase.id(250)
    def test_EmailInputScreen_TabRout_ElementsInFocus(self):

        # self.login_page.find_logo()

        body_tab = self.driver.find_element_by_tag_name("body")
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('recoveryCode', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Next', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Send a new email.', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Help', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Privacy', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Terms', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Privacy', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Help', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Send a new email.', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Next', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('recoveryCode', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('sub-title-email', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('navbar-brand', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('sub-title-email', value)
