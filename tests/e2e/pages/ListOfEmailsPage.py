import time
from tests.e2e.ConfigManager import ConfigManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class ListOfEmails:
    def __init__(self, driver) -> None:
        super().__init__()

        self.driver = driver


    def hover_over_select_all_checkbox(self):
        wait = WebDriverWait(self.driver, 10)
        select_all_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.page-actions .h-elem-select-all')))
        ActionChains(self.driver).move_to_element(select_all_checkbox).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def hover_over_refresh_icon(self):
        wait = WebDriverWait(self.driver, 10)
        refresh_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div [mattooltip="Refresh"]')))
        ActionChains(self.driver).move_to_element(refresh_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_refresh_icon(self):
        wait = WebDriverWait(self.driver, 10)
        refresh_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div [mattooltip="Refresh"]')))
        refresh_icon.click()

    def get_list_of_emails(self):
        wait = WebDriverWait(self.driver, 60)
        list_of_emails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table tbody .clickable')))
        return list_of_emails

    def hover_over_email_select_checkbox(self):
        wait = WebDriverWait(self.driver, 10)
        email_select_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.select-column .skip')))
        ActionChains(self.driver).move_to_element(email_select_checkbox).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_email_select_checkbox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.select-column .skip')))
        checkbox = self.driver.find_element_by_css_selector('.select-column .skip')
        checkbox.click()

    def get_starred_value_of_emails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(1) .favorite-column .skip img')))
        starred_status = self.driver.find_element_by_css_selector('tr:nth-child(1) .favorite-column .skip img')
        starred_value = starred_status.get_attribute('aria-describedby')
        return starred_value

    def open_email(self, emailNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(emailNumber) + ') .from-column')))
        email = self.driver.find_element_by_css_selector('tr:nth-child(' + str(emailNumber) + ') .from-column')
        email.click()

    def activate_email_checkbox(self, emailNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(emailNumber) +')' + ' .select-column .skip')))
        email = self.driver.find_element_by_css_selector('tr:nth-child(' + str(emailNumber) +')' + ' .select-column .skip')
        email.click()

    def get_mail_read_status(self, i):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(i) +') td.from-column span')))
        mail_read_status = self.driver.find_element_by_css_selector('tr:nth-child(' + str(i) +') td.from-column span').get_attribute('class')
        return mail_read_status

    def get_read_status_of_email_with_subject(self, messageSubject):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), " + "'" + messageSubject + "'" + ")]")))
        mail_read_status = self.driver.find_element_by_xpath("//*[contains(text(), " + "'" + messageSubject + "'" + ")]").get_attribute('class')
        return mail_read_status

    def open_kebab_menu_of_email(self, i):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(i) + ') .actions-column')))
        kebab_menu = self.driver.find_element_by_css_selector('tr:nth-child(' + str(i) + ') .actions-column')
        kebab_menu.click()

    def get_kebab_menu_item(self, emailNumber, menuItemNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(emailNumber) + ') .actions-column')))
        kebab_menu = self.driver.find_element_by_css_selector('tr:nth-child(' + str(emailNumber) + ') .actions-column')
        kebab_menu.click()
        kebab_menu_item = self.driver.find_element_by_css_selector('tr:nth-child(' +str(emailNumber) + ') li:nth-child(' + str(menuItemNumber) + ') a')
        return kebab_menu_item.text

    def click_kebab_menu_item(self, emailNumber, menuItemNumber):
        kebab_menu_item = self.driver.find_element_by_css_selector('tr:nth-child(' +str(emailNumber) + ') li:nth-child(' + str(menuItemNumber) + ') a')
        kebab_menu_item.click()

    def get_message_with_subject(self, messageSubject):
        try:
            self.driver.find_element_by_xpath('//*[contains(text(), "' + messageSubject + '")]')
        except NoSuchElementException:
            return False
        return True

    def open_message_with_subject(self, messageSubject):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), " + "'" + messageSubject + "'" + ")]")))
        email = self.driver.find_element_by_xpath("//*[contains(text(), " + "'" + messageSubject + "'" + ")]")
        email.click()

    def delete_message_with_subject(self, messageSubject):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), " + "'" + messageSubject + "'" + ")]")))
        email = self.driver.find_element_by_xpath("//*[contains(text(), " + "'" + messageSubject + "'" + ")]")
        email.click()

    def get_message_subject(self, emailNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr:nth-child(' + str(emailNumber) + ') td:nth-child(4) span')))
        email_subject = self.driver.find_element_by_css_selector('tr:nth-child(' + str(emailNumber) + ') td:nth-child(4) span')
        return email_subject.text

    def click_delete_icon(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mass-actions-area [mattooltip="Delete"]')))
        delete_icon = self.driver.find_element_by_css_selector('.mass-actions-area [mattooltip="Delete"]')
        delete_icon.click()

    def get_pagination_right_arrow_status(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.mat-paginator-navigation-next')))
        right_arrow = self.driver.find_element_by_css_selector('button.mat-paginator-navigation-next')
        return right_arrow.get_attribute('disabled')

    def click_pagination_right_arrow(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.mat-paginator-navigation-next')))
        right_arrow = self.driver.find_element_by_css_selector('button.mat-paginator-navigation-next')
        right_arrow.click()

    def get_add_star_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        add_star_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Add star"]')))
        ActionChains(self.driver).move_to_element(add_star_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_remove_star_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        remove_star_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Remove star"]')))
        ActionChains(self.driver).move_to_element(remove_star_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def get_mark_as_unread_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        mark_as_unread_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Mark As Unread"]')))
        ActionChains(self.driver).move_to_element(mark_as_unread_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_mark_as_unread_icon(self):
        wait = WebDriverWait(self.driver, 10)
        mark_as_unread_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Mark As Unread"]')))
        mark_as_unread_icon.click()

    def get_mark_as_read_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        mark_as_read_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Mark As Read"]')))
        ActionChains(self.driver).move_to_element(mark_as_read_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text

    def click_mark_as_read_icon(self):
        wait = WebDriverWait(self.driver, 10)
        mark_as_read_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Mark As Read"]')))
        mark_as_read_icon.click()

    def get_delete_icon_tooltip(self):
        wait = WebDriverWait(self.driver, 10)
        delete_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mass-actions-area a[mattooltip="Delete"]')))
        ActionChains(self.driver).move_to_element(delete_icon).perform()
        tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cdk-overlay-container .mat-tooltip')))
        return tooltip.text