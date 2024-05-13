from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class UuidPage:
    def __init__(self, browser):
        self.browser = browser

    def select_main_uuid_label(self) -> WebElement:
        uuid_label = self.browser.find_element(By.ID, 'uuid-label')
        return uuid_label

    def select_main_uuid_container(self) -> WebElement:
        uuid_container = self.browser.find_element(By.ID, 'uuid-container')
        return uuid_container

    def select_copy_main_btn(self) -> WebElement:
        copy_btn = self.browser.find_element(By.ID, 'copy-uuid-button')
        return copy_btn

    def select_generate_main_uuid_btn(self) -> WebElement:
        copy_btn = self.browser.find_element(By.ID, 'generate-uuid-button')
        return copy_btn

    def select_uuid_version_label(self) -> WebElement:
        copy_btn = self.browser.find_element(By.ID, 'select-uuid-version-label')
        return copy_btn

    def select_uuid_version_radio_group(self) -> WebElement:
        group = self.browser.find_element(By.ID, 'uuid-version-selection-group')
        return group

    def select_uuid_v1_radio_option(self) -> WebElement:
        v1_option = self.browser.find_element(By.ID, 'uuid-version-selection-v1')
        return v1_option

    def select_uuid_v4_radio_option(self) -> WebElement:
        v4_option = self.browser.find_element(By.ID, 'uuid-version-selection-v4')
        return v4_option

    def select_uuid_v7_radio_option(self) -> WebElement:
        v7_option = self.browser.find_element(By.ID, 'uuid-version-selection-v7')
        return v7_option

    def select_uuid_bulk_count_field(self) -> WebElement:
        count_field = self.browser.find_element(By.ID, 'uuid-count-field')
        return count_field

    def select_uuid_bulk_generation_btn(self) -> WebElement:
        count_field = self.browser.find_element(By.ID, 'uuid-count-generate')
        return count_field

    def select_bulk_generated_uuids(self) -> list[WebElement]:
        multiple_uuid_wrapper: WebElement = self.browser.find_element(By.ID, 'multiple-uuid-generated-wrapper')
        multiple_uuids = multiple_uuid_wrapper.find_elements(By.CLASS_NAME, 'bulk-uuid-item')
        return multiple_uuids
