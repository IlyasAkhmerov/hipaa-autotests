import unittest
from qaseio.pytest import qase
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.SupportPage import SupportPage
from selenium.webdriver.common.keys import Keys


# _________________________________________________________________________________
# В тесте проверяются кейсы для экрана ввода емейла
# _________________________________________________________________________________

class EmailInputScreenTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.support_page = SupportPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    @qase.id(3)
    def test_EmailInputScreen_Logo_Correct(self):
        logo = self.login_page.get_logo()
        self.assertEqual('TruVISIBILITY SecureMail', logo)

    @qase.id(3)
    def test_EmailInputScreen_StepName_Correct(self):
        step_name = self.login_page.get_step_name()
        self.assertEqual('SecureMail Sign In', step_name)

    @qase.id(3)
    def test_EmailInputScreen_StaySignedCheckbox_Present(self):
        checkbox = self.login_page.get_StaySigned_checkbox()
        self.assertEqual('Stay signed in for a week', checkbox)

    @qase.id(3)
    def test_EmailInputScreen_HelpLink_Present(self):
        help_link = self.login_page.get_help_link()
        self.assertEqual('Help', help_link)

    @qase.id(3)
    def test_EmailInputScreen_PrivacyLink_Present(self):
        privacy_link = self.login_page.get_privacy_link()
        self.assertEqual('Privacy', privacy_link)

    @qase.id(3)
    def test_EmailInputScreen_TermsLink_Present(self):
        terms_link = self.login_page.get_terms_link()
        self.assertEqual('Terms', terms_link)

    @qase.id(310, 131)
    def test_EmailInputScreen_EmptyEmailField_ErrorMessage(self):

        self.login_page.enter_email('')
        error_message = self.login_page.get_response_message()
        self.assertEqual('Email address is incorrect', error_message)

    @qase.id(4, 131)
    def test_EmailInputScreen_WrongEmail_ErrorMessage(self):

        config = ConfigManager.get_config()
        unregistered_email = config.unregistered_email
        self.login_page.enter_email(unregistered_email)
        error_message = self.login_page.get_response_message()
        self.assertEqual('Email address is incorrect', error_message)

    @qase.id(3)
    def test_EmailInputScreen_ValidEmail_Success(self):

        config = ConfigManager.get_config()
        valid_email = config.secure_email

        self.login_page.enter_email(valid_email)
        password_field = self.password_page.get_password_placeholder()
        self.assertEqual('Password', password_field)

    @qase.id(6)
    def test_EmailInputScreen_ClickHelpLink_Success(self):

        self.login_page.click_help_link()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        current_link = self.support_page.get_current_url()
        self.assertEqual('https://support.truvisibility.com/TruMailServer', current_link)

        support_page_title = self.support_page.get_page_title()
        self.assertEqual('How can we help?', support_page_title)

    @qase.id(6)
    def test_EmailInputScreen_ClickPrivacyLink_Success(self):

        self.login_page.click_privacy_link()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        current_link = self.support_page.get_current_url()
        self.assertEqual('https://www.truvisibility.com/privacy-policy/', current_link)

    @qase.id(6)
    def test_EmailInputScreen_ClickTermsLink_Success(self):

        self.login_page.click_terms_link()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        current_link = self.support_page.get_current_url()
        self.assertEqual('https://www.truvisibility.com/terms-of-service/', current_link)

    '''Перемещение по элементам с помощью клавиш Tab и Shif+Tab'''

    @qase.id(246)
    def test_EmailInputScreen_TabRout_ElementsInFocus(self):

        self.login_page.get_logo()

        body_tab = self.driver.find_element(By.TAG_NAME, "body")
        # body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('email', value)

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
        self.assertEqual('Next', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('type')
        self.assertEqual('checkbox', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('email', value)

        body_tab.send_keys(Keys.SHIFT + Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('navbar-brand', value)



