import unittest
from qaseio.pytest import qase
import time
from selenium import webdriver
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.LeftSidebar import LeftSidebar
from selenium.webdriver.common.keys import Keys

# _________________________________________________________________________________
# В тесте проверяются кейсы для экрана ввода пароля
# _________________________________________________________________________________

class PasswordInputScreenTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()
        registred_email = config.secure_email

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.leftsidebar_page = LeftSidebar(self.driver)

        self.login_page.enter_email(registred_email)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    @qase.id(3)
    def test_PasswordInputScreen_PasswordPlaceholder_Present(self):
        password_field = self.password_page.get_password_placeholder()
        self.assertEqual('Password', password_field)

    @qase.id(3)
    def test_PasswordInputScreen_Logo_Correct(self):
        logo = self.password_page.get_logo()
        self.assertEqual('TruVISIBILITY SecureMail', logo)
        print(logo)

    @qase.id(3)
    def test_PasswordInputScreen_StepName_Correct(self):
        step_name = self.password_page.get_step_name()
        self.assertEqual('SecureMail Sign In', step_name)

    @qase.id(3)
    def test_PasswordInputScreen_Email_Present(self):
        email = self.password_page.get_email()
        config = ConfigManager.get_config()
        login = config.secure_email
        self.assertEqual(login, email)

    @qase.id(3)
    def test_PasswordInputScreen_ShowPasswordCheckbox_Present(self):
        checkbox = self.password_page.get_ShowPassword_checkbox()
        self.assertEqual('Show password', checkbox)

    @qase.id(3)
    def test_PasswordInputScreen_HelpLink_Present(self):
        help_link = self.password_page.get_help_link()
        self.assertEqual('Help', help_link)

    @qase.id(3)
    def test_PasswordInputScreen_PrivacyLink_Present(self):
        privacy_link = self.password_page.get_privacy_link()
        self.assertEqual('Privacy', privacy_link)

    @qase.id(3)
    def test_PasswordInputScreen_TermsLink_Present(self):
        terms_link = self.password_page.get_terms_link()
        self.assertEqual('Terms', terms_link)

    @qase.id(5, 131)
    def test_PasswordInputScreen_EmptyPasswordField_ErrorMessage(self):

        self.password_page.enter_password('')
        self.password_page.click_next_button()
        error_message = self.password_page.get_response_message()
        self.assertEqual('Password is incorrect', error_message)

    @qase.id(5, 131)
    def test_PasswordInputScreen_WrongPassword_ErrorMessage(self):

        config = ConfigManager.get_config()
        wrong_password = config.wrong_password
        self.password_page.enter_password(wrong_password)
        self.password_page.click_next_button()
        error_message = self.login_page.get_response_message()
        self.assertEqual('Password is incorrect', error_message)

    @qase.id(131)
    def test_PasswordInputScreen_ActivateShowPasswordCheckbox_Activated(self):

        config = ConfigManager.get_config()
        valid_password = config.password

        self.password_page.enter_password(valid_password)
        self.password_page.activate_ShowPassword_checkbox()
        password_field = self.password_page.get_password_field()
        password_type = password_field.get_attribute('type')
        time.sleep(1)
        self.assertEqual('text', password_type)

    @qase.id(3)
    def test_PasswordRecovery_ForgotPasswordLink_Present(self):

        forgot_password_link = self.password_page.get_forgot_password_link()
        self.assertEqual('Forgot Password?', forgot_password_link)

    @qase.id(3)
    def test_PasswordInputScreen_ValidPassword_Success(self):

        config = ConfigManager.get_config()
        valid_password = config.password

        self.password_page.enter_password(valid_password)
        self.password_page.click_next_button()
        inbox_folder = self.leftsidebar_page.get_inbox_folder()
        self.assertEqual('Inbox', inbox_folder)

    '''Перемещение по элементам с помощью клавиш Tab и Shif+Tab'''

    @qase.id(247)
    def test_PasswordInputScreen_TabRout_ElementsInFocus(self):

        self.password_page.get_logo()

        body_tab = self.driver.find_element_by_tag_name("body")
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('password', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('type')
        self.assertEqual('checkbox', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Next', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('forgot-password', value)

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
        value = active_element.get_attribute('class')
        self.assertEqual('forgot-password', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Next', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('type')
        self.assertEqual('checkbox', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('password', value)

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






