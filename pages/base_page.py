import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators


class Base_Page:

    def __init__(self, driver):
        self.locator = Locators
        self.driver = driver

    def get_element(self, locator):
        # return self.driver.find_element(*locator)
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator) or
                                                    EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_at(self, locator, data):
        self.get_element(locator).send_keys(data)

    def press_ctrl_a(self, locator):
        self.get_element(locator).send_keys(Keys.CONTROL, "a")

    def press_delete(self, locator):
        self.get_element(locator).send_keys(Keys.DELETE)

    def click_by_mouse(self, locator):
        action = ActionChains(self.driver)
        element = self.get_element(locator)
        action.move_to_element(element).click(element).perform()

    def get_text(self, locator):
        text = self.get_element(locator).text
        return text

    def is_enabled(self, locator):
        return self.get_element(locator).is_enabled()

    def is_selected(self, locator):
        return self.get_element(locator).is_selected()

    def perform_drag_and_drop(self, source_location, destination_location):
        action = ActionChains(self.driver)
        drag = self.get_element(source_location)
        drop = self.get_element(destination_location)
        action.drag_and_drop(drag, drop).perform()

    def switch_to_iframe(self, locator):
        self.driver.switch_to.frame(self.get_element(locator))

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def scroll_into_view(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_into_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_active_tab(self):
        # self.driver.switch_to.new_window('tab')
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_new_window(self):
        self.driver.switch_to.new_window('window')
