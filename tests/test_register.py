import time
from tests.base_test import Base_Test
from pages.registration_page import Registration_Page
from testdata.data import Data


class Registration_Test(Base_Test):
    def test_registration_data(self):
        rp = Registration_Page(self.driver)
        rp.enter_first_name(Data.FIRSTNAME)
        time.sleep(2)
        rp.enter_last_name(Data.LASTNAME)
        time.sleep(2)
        rp.enter_address(Data.ADDRESS)
        time.sleep(3)
        rp.enter_email(Data.Email)
        time.sleep(3)
        rp.enter_phone(Data.PHONE)
        time.sleep(3)
        rp.select_language()
        rp.select_skills()
        time.sleep(2)
        rp.enter_password(Data.FIRST_PASSWORD)
        time.sleep(3)
        rp.enter_second_password(Data.CONFIRM_PASSWORD)
        time.sleep(3)
        rp.upload_photo()
        time.sleep(10)
        rp.select_year()
        time.sleep(3)
        rp.select_month()
        time.sleep(3)
        rp.select_day()
        time.sleep(3)

    def test_radio_button(self):
        rp = Registration_Page(self.driver)
        time.sleep(2)
        print(f" Should: False------>{rp.is_female_radio_button_selected()}")
        rp.select_male()
        print(f"Should: True--------->{rp.is_male_radio_button_selected()}")
        time.sleep(5)
        print(f"Should: False--------->{rp.is_female_radio_button_selected()}")
        rp.select_female()
        print(f"Should: True--------->{rp.is_female_radio_button_selected()}")
        time.sleep(5)

    def test_checkbox(self):
        rp = Registration_Page(self.driver)
        time.sleep(2)
        print(f"Should: False ==== {rp.is_cricket_checkbox_selected()}")
        rp.select_cricket()
        print(f"Should: True ==== {rp.is_cricket_checkbox_selected()}")
        time.sleep(2)
