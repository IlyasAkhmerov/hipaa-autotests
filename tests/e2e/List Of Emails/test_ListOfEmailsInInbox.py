import unittest
from qaseio.pytest import qase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.ConfigManager import ConfigManager
from tests.e2e.pages.LoginPage import LoginPage
from tests.e2e.pages.PasswordPage import PasswordPage
from tests.e2e.pages.LeftSidebar import LeftSidebar
from tests.e2e.pages.ListOfEmailsPage import ListOfEmails
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


        self.password_page.authorization(email=email, password=password)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()


    @qase.id(111)
    def test_ListOfEmailsInbox_SelectAllCheckboxHoverOver_TooltipAppears(self):
        leftsidebar_status = self.list_of_emails_page.hover_over_select_all_checkbox()
        self.assertEqual('Select all', leftsidebar_status)

    @qase.id(111)
    def test_ListOfEmailsInbox_RefreshIconHoverOver_TooltipAppears(self):
        leftsidebar_status = self.list_of_emails_page.hover_over_refresh_icon()
        self.assertEqual('Refresh', leftsidebar_status)

    @qase.id(111)
    def test_ListOfEmailsInbox_ActionPaneAddStarHoverOver_TooltipAppears(self):
        self.list_of_emails_page.activate_email_checkbox(5)
        add_star_tooltip = self.list_of_emails_page.get_add_star_icon_tooltip()
        self.assertEqual('Add star', add_star_tooltip)

    @qase.id(111)
    def test_ListOfEmailsInbox_ActionPanelRemoveStarHoverOver_TooltipAppears(self):
        self.list_of_emails_page.activate_email_checkbox(5)
        remove_star_tooltip = self.list_of_emails_page.get_remove_star_icon_tooltip()
        self.assertEqual('Remove star', remove_star_tooltip)

    @qase.id(111)
    def test_ListOfEmailsInbox_ActionPanelMarkAsUnreadHoverOver_TooltipAppears(self):
        self.list_of_emails_page.activate_email_checkbox(5)
        mark_as_unread_tooltip = self.list_of_emails_page.get_mark_as_unread_icon_tooltip()
        self.assertEqual('Mark As Unread', mark_as_unread_tooltip)

    @qase.id(111)
    def test_ListOfEmailsInbox_ActionPanelMarkAsReadHoverOver_TooltipAppears(self):
        self.list_of_emails_page.activate_email_checkbox(5)
        mark_as_read_tooltip = self.list_of_emails_page.get_mark_as_read_icon_tooltip()
        self.assertEqual('Mark As Read', mark_as_read_tooltip)

    @qase.id(111)
    def test_ListOfEmailsInbox_ActionPanelDeleteHoverOver_TooltipAppears(self):
        self.list_of_emails_page.activate_email_checkbox(5)
        delete_tooltip = self.list_of_emails_page.get_delete_icon_tooltip()
        self.assertEqual('Delete', delete_tooltip)


    '''Проверка появление тултипа при наведение на чекбокс каждого письма в списке'''

    @qase.id(111)
    def test_ListOfEmailsInbox_SelectEmailIconHoverOver_TooltipAppears(self):
        list_of_emails = self.list_of_emails_page.get_list_of_emails()
        i = 1
        while i <= len(list_of_emails):
            select_email_checkbox = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(' + str(i) +')' + ' .select-column .skip')
            ActionChains(self.driver).move_to_element(select_email_checkbox).perform()
            tooltip = self.driver.find_element(By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')
            self.assertEqual('Select', tooltip.text)
            i += 1

    '''Проверка появление тултипа при наведение на иконку звездочки каждого письма в списке'''

    @qase.id(111)
    def test_ListOfEmailsInbox_StarredIconHoverOver_TooltipAppears(self):
        list_of_emails = self.list_of_emails_page.get_list_of_emails()
        i = 1
        while i <= len(list_of_emails):
            select_starred_icon = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(' + str(i) +')' + ' .favorite-column .skip')
            starred_status = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(' + str(i) +')' + ' .skip img')
            starred_value = starred_status.get_attribute('aria-describedby')
            ActionChains(self.driver).move_to_element(select_starred_icon).perform()
            tooltip = self.driver.find_element(By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')
            if starred_value == 'cdk-describedby-message-9':
                self.assertEqual('Not starred', tooltip.text)
                print(tooltip.text)
            else:
                self.assertEqual('Starred', tooltip.text)
                print(tooltip.text)
            i += 1

    '''Проверка появление тултипа при наведение на кебаб меню каждого письма в списке'''

    @qase.id(111)
    def test_ListOfEmailsInbox_EmailsKebabMenuHoverOver_TooltipAppears(self):
        list_of_emails = self.list_of_emails_page.get_list_of_emails()
        i = 1
        while i <= len(list_of_emails):
            kebab_menu = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(' + str(i) + ')' + ' .actions-column')
            ActionChains(self.driver).move_to_element(kebab_menu).perform()
            tooltip = self.driver.find_element(By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')
            self.assertEqual('Actions', tooltip.text)
            i += 1

    @qase.id(111)
    def test_ListOfEmailsInbox_Checkbox_Activate(self):
        list_of_emails = self.list_of_emails_page.get_list_of_emails()
        i = 1
        while i <= (len(list_of_emails) - 1):
            self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(' + str(i) +')' + ' .select-column .skip').click()
            i += 1
        print("The End")

    '''Проверка элементов кебаб меню письма в списке'''

    @qase.id(113)
    def test_ListOfEmailsInbox_KebabMenuOpen_CorrectMenuItem(self):
        self.list_of_emails_page.get_list_of_emails()
        sender = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) .from-column span')
        message_status = sender.get_attribute('class')
        kebab_menu = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) .actions-column')
        kebab_menu.click()
        first_menu_item = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) li:nth-child(1) a')
        second_menu_item = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) li:nth-child(2) a')
        if message_status == 'unread':
            self.assertEqual('Mark As Read', first_menu_item.text)
            self.assertEqual('Delete', second_menu_item.text)
            first_menu_item.click()
            message_status = sender.get_attribute('class')
            self.assertEqual('', message_status)
            kebab_menu.click()
            self.assertEqual('Mark As Unread', first_menu_item.text)
            self.assertEqual('Delete', second_menu_item.text)
        else:
            self.assertEqual('Mark As Unread', first_menu_item.text)
            self.assertEqual('Delete', second_menu_item.text)
            first_menu_item.click()
            self.assertEqual('', message_status)
            kebab_menu.click()
            self.assertEqual('Mark As Read', first_menu_item.text)
            self.assertEqual('Delete', second_menu_item.text)


    '''Отметка письма как прочитанное/непрочитанное с помощью кебаб-меню'''

    @qase.id(69, 71)
    def test_ListOfEmailsInbox_MarkAsReadUnread_Success(self):
        self.list_of_emails_page.get_list_of_emails()
        kebab_menu_item = self.list_of_emails_page.get_kebab_menu_item(1, 1)
        if kebab_menu_item == 'Mark As Read':
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('unread', email_read_status)
            self.list_of_emails_page.click_kebab_menu_item(1, 1)
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('', email_read_status)
            kebab_menu_item = self.list_of_emails_page.get_kebab_menu_item(1, 1)
            self.assertEqual('Mark As Unread', kebab_menu_item)
            self.list_of_emails_page.click_kebab_menu_item(1, 1)
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('unread', email_read_status)
        else:
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('', email_read_status)
            self.list_of_emails_page.click_kebab_menu_item(1, 1)
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('unread', email_read_status)
            kebab_menu_item = self.list_of_emails_page.get_kebab_menu_item(1, 1)
            self.assertEqual('Mark As Read', kebab_menu_item)
            self.list_of_emails_page.click_kebab_menu_item(1, 1)
            email_read_status = self.list_of_emails_page.get_mail_read_status(1)
            self.assertEqual('', email_read_status)

    @qase.id(72, 73)
    def test_ListOfEmailsInbox_MarkAsReadUnread_Success(self):
        self.list_of_emails_page.get_list_of_emails()
        mail_read_status = self.list_of_emails_page.get_mail_read_status(5)
        self.list_of_emails_page.activate_email_checkbox(5)
        if mail_read_status == 'unread':
            self.list_of_emails_page.click_mark_as_read_icon()
            email_read_status = self.list_of_emails_page.get_mail_read_status(5)
            self.assertEqual('', email_read_status)
            self.list_of_emails_page.click_mark_as_unread_icon()
            email_read_status = self.list_of_emails_page.get_mail_read_status(5)
            self.assertEqual('unread', email_read_status)
        else:
            self.list_of_emails_page.click_mark_as_unread_icon()
            email_read_status = self.list_of_emails_page.get_mail_read_status(5)
            self.assertEqual('unread', email_read_status)
            self.list_of_emails_page.click_mark_as_read_icon()
            email_read_status = self.list_of_emails_page.get_mail_read_status(5)
            self.assertEqual('', email_read_status)

