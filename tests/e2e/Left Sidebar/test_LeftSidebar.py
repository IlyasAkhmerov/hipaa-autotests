import unittest
import time
from selenium import webdriver
from qaseio.pytest import qase
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.LeftSidebar import LeftSidebar

# _________________________________________________________________________________
# В тесте проверяются кейсы для левого сайдбара
# _________________________________________________________________________________

class LeftSidebarTestCases(unittest.TestCase):
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


        self.password_page.authorization(email=email, password=password)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()


    @qase.id(115)
    def test_LeftSideBar_LeftSideBarStatus_Expanded(self):

        leftsidebar_status = self.leftsidebar_page.get_leftsidebar_status()
        self.assertEqual('sidebarleft', leftsidebar_status)

    @qase.id(115)
    def test_LeftSideBar_InboxFolder_PresentAndActive(self):

        inbox_folder = self.leftsidebar_page.get_inbox_folder()
        inbox_folder_status = self.leftsidebar_page.get_inbox_folder_status()
        self.assertEqual('Inbox', inbox_folder)
        self.assertEqual('folder active', inbox_folder_status)

    @qase.id(115)
    def test_LeftSideBar_SentFolder_PresentAndNotActive(self):

        sent_folder = self.leftsidebar_page.get_sent_folder()
        sent_folder_status = self.leftsidebar_page.get_sent_folder_status()
        self.assertEqual('Sent', sent_folder)
        self.assertEqual('folder', sent_folder_status)

    @qase.id(115)
    def test_LeftSideBar_NewEmailButton_Present(self):

        new_email_button = self.leftsidebar_page.get_new_email_button()
        self.assertEqual(' New Email', new_email_button)

    @qase.id(115)
    def test_LeftSideBar_OpenCollapsePanel_Success(self):

        self.leftsidebar_page.collapse_leftsidebar()
        leftsidebar_status = self.leftsidebar_page.get_leftsidebar_status()
        self.assertEqual('sidebarleft slim', leftsidebar_status)

        self.leftsidebar_page.expand_leftsidebar()
        leftsidebar_status = self.leftsidebar_page.get_leftsidebar_status()
        self.assertEqual('sidebarleft', leftsidebar_status)

    @qase.id(117)
    def test_LeftSideBar_HoverOverMenuIcon_TooltipIsPresent(self):

        menu_icon = self.leftsidebar_page.hover_over_menu_icon()
        self.assertEqual('Main menu', menu_icon)

    @qase.id(117)
    def test_LeftSideBar_HoverOverNewEmailButton_TooltipIsPresent(self):

        self.leftsidebar_page.collapse_leftsidebar()
        new_email_tooltip = self.leftsidebar_page.hover_over_new_email_button()
        self.assertEqual('New Email', new_email_tooltip)

    @qase.id(117)
    def test_LeftSideBar_HoverOverInboxFolder_TooltipIsPresent(self):

        self.leftsidebar_page.collapse_leftsidebar()
        inbox_folder_tooltip = self.leftsidebar_page.hover_over_inbox_folder()
        self.assertEqual('Inbox', inbox_folder_tooltip)

    @qase.id(117)
    def test_LeftSideBar_HoverOverSentFolder_TooltipIsPresent(self):

        self.leftsidebar_page.collapse_leftsidebar()
        inbox_folder_tooltip = self.leftsidebar_page.hover_over_sent_folder()
        self.assertEqual('Sent', inbox_folder_tooltip)

    @qase.id(116)
    def test_LeftSideBar_GoToSentFolderWhenSidebarIsExpanded_Success(self):

        self.leftsidebar_page.click_sent_folder()
        sent_folder_status = self.leftsidebar_page.get_sent_folder_status()
        self.assertEqual('folder active', sent_folder_status)

    @qase.id(116)
    def test_LeftSideBar_GoToSentFolderWhenSidebarIsCollapsed_Success(self):

        self.leftsidebar_page.collapse_leftsidebar()
        self.leftsidebar_page.click_sent_folder()
        sent_folder_status = self.leftsidebar_page.get_sent_folder_status()
        self.assertEqual('folder active', sent_folder_status)
