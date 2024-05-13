import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from classes.test_uuid import TestUuid
from classes.uuid_page import UuidPage
import tkinter as tk


class ChromeTestCases(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:3000')
        self.page = UuidPage(self.browser)
        self.addCleanup(self.browser.quit)

    def test_all_text_labels_is_correct(self):
        uuid_label = self.page.select_main_uuid_label()
        self.assertEqual('Сгенерированный UUID:', uuid_label.text)

        btn = self.page.select_copy_main_btn()
        self.assertEqual('Скопировать', btn.text)

        btn = self.page.select_generate_main_uuid_btn()
        self.assertEqual('Сгенерировать', btn.text)

        btn = self.page.select_generate_main_uuid_btn()
        self.assertEqual('Сгенерировать', btn.text)

        label = self.page.select_uuid_version_label()
        self.assertEqual('Выберите версию UUID', label.text)

        field = self.page.select_uuid_bulk_count_field()
        self.assertEqual('10', field.get_attribute('placeholder'))

        radio_option = self.page.select_uuid_v1_radio_option()
        radio_option_label = radio_option.find_element(By.CSS_SELECTOR, 'label')
        self.assertEqual('version 1 UUID', radio_option_label.text)

        radio_option = self.page.select_uuid_v4_radio_option()
        radio_option_label = radio_option.find_element(By.CSS_SELECTOR, 'label')
        self.assertEqual('version 4 UUID', radio_option_label.text)

        radio_option = self.page.select_uuid_v7_radio_option()
        radio_option_label = radio_option.find_element(By.CSS_SELECTOR, 'label')
        self.assertEqual('version 7 UUID', radio_option_label.text)

    def test_init_state_is_correct(self):
        main_uuid = self.page.select_main_uuid_container()
        test_uuid = TestUuid(main_uuid.text, 4)
        self.assertEqual(True, test_uuid.is_valid_uuid())

        default_radio_option = self.page.select_uuid_v4_radio_option()
        default_radio_option_control = default_radio_option.find_element(By.CSS_SELECTOR, 'input')
        self.assertEqual('true', default_radio_option_control.get_attribute('checked'))

        bulk_count_input_field = self.page.select_uuid_bulk_count_field()
        bulk_count_input_field_value = bulk_count_input_field.get_attribute('value')
        self.assertEqual('', bulk_count_input_field_value)

        bulk_uuids = self.page.select_bulk_generated_uuids()
        self.assertEqual(0, len(bulk_uuids))

    def test_new_uuid_generation_is_unique(self):
        main_uuid = self.page.select_main_uuid_container()
        first_uuid = main_uuid.text

        self.browser.refresh()

        main_uuid = self.page.select_main_uuid_container()
        second_uuid = main_uuid.text

        self.assertNotEqual(first_uuid, second_uuid)

        generate_btn = self.page.select_generate_main_uuid_btn()
        generate_btn.click()

        main_uuid = self.page.select_main_uuid_container()
        regenerated_uuid = main_uuid.text

        self.assertNotEqual(second_uuid, regenerated_uuid)

    def test_uuid_v1_is_correct(self):
        default_radio_option = self.page.select_uuid_v1_radio_option()
        default_radio_option_control = default_radio_option.find_element(By.CSS_SELECTOR, 'input')
        default_radio_option_control.click()

        main_uuid = self.page.select_main_uuid_container()
        generated_uuid_v1 = main_uuid.text
        test_uuid = TestUuid(generated_uuid_v1, 1)
        self.assertEqual(True, test_uuid.is_valid_uuid())

    def test_uuid_v4_is_correct(self):
        default_radio_option = self.page.select_uuid_v4_radio_option()
        default_radio_option_control = default_radio_option.find_element(By.CSS_SELECTOR, 'input')
        default_radio_option_control.click()

        main_uuid = self.page.select_main_uuid_container()
        generated_uuid_v4 = main_uuid.text
        test_uuid = TestUuid(generated_uuid_v4, 4)
        self.assertEqual(True, test_uuid.is_valid_uuid())

    def test_clipboard_uuid(self):
        main_uuid = self.page.select_main_uuid_container()
        generated_uuid_v1 = main_uuid.text

        copy_btn = self.page.select_copy_main_btn()
        copy_btn.click()

        root = tk.Tk()
        root.withdraw()
        clipboard_content = root.clipboard_get()

        self.assertEqual(generated_uuid_v1, clipboard_content)

    def test_bulk_generate_v1(self):
        radio_option = self.page.select_uuid_v1_radio_option()
        radio_option_control = radio_option.find_element(By.CSS_SELECTOR, 'input')
        radio_option_control.click()

        bulk_count_input = self.page.select_uuid_bulk_count_field()
        bulk_count_input.send_keys("10")

        bulk_generation_btn = self.page.select_uuid_bulk_generation_btn()
        bulk_generation_btn.click()

        generated_elems = self.page.select_bulk_generated_uuids()
        self.assertEqual(10, len(generated_elems))

        for generated_elem in generated_elems:
            generated_uuid = generated_elem.text
            test_uuid = TestUuid(generated_uuid, 1)
            self.assertEqual(True, test_uuid.is_valid_uuid())

    def test_bulk_generate_v4(self):
        radio_option = self.page.select_uuid_v4_radio_option()
        radio_option_control = radio_option.find_element(By.CSS_SELECTOR, 'input')
        radio_option_control.click()

        bulk_count_input = self.page.select_uuid_bulk_count_field()
        bulk_count_input.send_keys("10")

        bulk_generation_btn = self.page.select_uuid_bulk_generation_btn()
        bulk_generation_btn.click()

        generated_elems = self.page.select_bulk_generated_uuids()
        self.assertEqual(10, len(generated_elems))

        for generated_elem in generated_elems:
            generated_uuid = generated_elem.text
            test_uuid = TestUuid(generated_uuid, 4)
            self.assertEqual(True, test_uuid.is_valid_uuid())

    def test_clearing_state_after_version_reselection(self):
        bulk_count_input = self.page.select_uuid_bulk_count_field()
        bulk_count_input.send_keys("10")
        bulk_generation_btn = self.page.select_uuid_bulk_generation_btn()
        bulk_generation_btn.click()

        radio_option = self.page.select_uuid_v1_radio_option()
        radio_option_control = radio_option.find_element(By.CSS_SELECTOR, 'input')
        radio_option_control.click()

        bulk_input_value = bulk_count_input.get_attribute("value")
        self.assertEqual('', bulk_input_value)

        generated_elems = self.page.select_bulk_generated_uuids()
        self.assertEqual(0, len(generated_elems))


    def test_restriction_of_count_field(self):
        bulk_count_input = self.page.select_uuid_bulk_count_field()
        bulk_count_input.send_keys("1000")
        bulk_input_value = bulk_count_input.get_attribute("value")
        self.assertEqual('10', bulk_input_value)

        bulk_count_input.send_keys(Keys.BACKSPACE)
        bulk_count_input.send_keys(Keys.BACKSPACE)

        bulk_count_input.send_keys("1a")
        bulk_input_value = bulk_count_input.get_attribute("value")
        self.assertEqual('1', bulk_input_value)

        bulk_count_input.send_keys(Keys.BACKSPACE)

        bulk_count_input.send_keys("00")
        bulk_input_value = bulk_count_input.get_attribute("value")
        self.assertEqual('00', bulk_input_value)

    def test_clearing_of_bulk_generation_with_zero_count(self):
        bulk_count_input = self.page.select_uuid_bulk_count_field()
        bulk_count_input.send_keys("10")
        bulk_generation_btn = self.page.select_uuid_bulk_generation_btn()
        bulk_generation_btn.click()

        bulk_count_input.send_keys(Keys.BACKSPACE)
        bulk_count_input.send_keys(Keys.BACKSPACE)

        bulk_count_input.send_keys("00")

        bulk_generation_btn.click()

        generated_elems = self.page.select_bulk_generated_uuids()
        self.assertEqual(0, len(generated_elems))


if __name__ == '__main__':
    unittest.main()
