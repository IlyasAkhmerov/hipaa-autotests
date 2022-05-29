import unittest
from qaseio.pytest import qase
import time
from selenium import webdriver
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.LeftSidebar import LeftSidebar
from tests.e2e.pages.ListOfEmailsPage import ListOfEmails
from tests.e2e.pages.ViewEmailPage import ViewEmail
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# _________________________________________________________________________________
# В тесте проверяются кейсы для списка писем в папке Входящие
# _________________________________________________________________________________

class ListOfEmailsInbox(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()
        email = config.secure_email
        password = config.password

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(config.driver_path, options=options)
        self.driver.get(config.staging_url)

        self.login_page = LoginPage(self.driver)
        self.password_page = PasswordPage(self.driver)
        self.leftsidebar_page = LeftSidebar(self.driver)
        self.list_of_emails_page = ListOfEmails(self.driver)
        self.view_email_page = ViewEmail(self.driver)


        self.password_page.authorization(email=email, password=password)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()


        '''Открытие элементов с использованием клавиш Enter и Space'''

    @qase.id(277)
    def test_ListOfEmailsInbox_OpeningItemsByPressingSpaceOrEnter_Success(self):
        self.list_of_emails_page.get_list_of_emails()
        body_tab = self.driver.find_element_by_tag_name("body")

        body_tab.send_keys(',')
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('select-all-message-checkbox', value)

        body_tab.send_keys(Keys.ARROW_DOWN)

        active_element = self.driver.switch_to.active_element
        body_tab.send_keys(Keys.ENTER)
        self.view_email_page.get_back_arrow()
        self.view_email_page.click_back_arrow()

        body_tab.send_keys(Keys.ARROW_LEFT)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('folder0', value)

        body_tab.send_keys(Keys.ARROW_DOWN)
        active_element = self.driver.switch_to.active_element
        value = active_element.get_attribute('id')
        self.assertEqual('folder1', value)
