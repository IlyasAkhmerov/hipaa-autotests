import unittest
from qaseio.pytest import qase
import time
from selenium import webdriver
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.PasswordRecoveryPage import PasswordRecoveryPage
from selenium.webdriver.common.keys import Keys

from tests.e2e.pages.LeftSidebar import LeftSidebar

# _________________________________________________________________________________
# В тесте проверяются кейсы восстановления пароля
# _________________________________________________________________________________

class PasswordRecoveryTestCases(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()
        without_alternative_email = config.without_alternative_email

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.password_recovery_page = PasswordRecoveryPage(self.driver)
        #self.leftsidebar_page = LeftSidebar(self.driver)


        self.login_page.enter_email(without_alternative_email)
        self.password_recovery_page.click_forgot_password_link()

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()



    @qase.id(22)
    def test_PasswordRecovery_NoAlternativeEmail_WarningMessage(self):

        info_message = self.password_recovery_page.get_information_message()
        self.assertEqual("We couldn't fully identify this account. Please contact your SecureMail account administrator for assistance.", info_message)

    @qase.id(22)
    def test_PasswordRecovery_NoAlternativeEmail_NextButtonIsPresent(self):

        sign_in_button = self.password_recovery_page.get_SignIn_button()
        self.assertEqual('Sign In', sign_in_button)

    @qase.id(22)
    def test_PasswordRecovery_NoAlternativeEmailClickNextButton_GoToAuthorizationPage(self):

        self.password_recovery_page.click_SignIn_button()
        step_name = self.login_page.get_step_name()
        self.assertEqual('SecureMail Sign In', step_name)

    '''Перемещение по элементам с помощью клавиш Tab и Shif+Tab'''

    @qase.id(252)
    def test_EmailInputScreen_TabRout_ElementsInFocus(self):

        body_tab = self.driver.find_element_by_tag_name("body")

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('class')
        self.assertEqual('sub-title-email', value)

        body_tab.send_keys(Keys.TAB)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('innerHTML')
        self.assertEqual('Sign In', value)

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
        self.assertEqual('Sign In', value)

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



