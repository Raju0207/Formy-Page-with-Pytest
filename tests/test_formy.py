import time
from tests.base_test import Base_Test
from pages.formy_page import Formy_Page
from testdata.data import Data
import pytest


class Test_Formy(Base_Test):

    @pytest.mark.sanity
    def test_formy_autocomplete_data(self):
        acp = Formy_Page(self.driver)
        # Autocomplete Page
        acp.select_autocomplete()
        time.sleep(2)
        acp.enter_address(Data.ADDRESS)
        time.sleep(2)
        acp.select_ok_button()
        time.sleep(2)
        acp.enter_street_address(Data.STREETADDRESS)
        time.sleep(2)
        acp.enter_street_address2(Data.STREETADDRESS2)
        time.sleep(2)
        acp.enter_city(Data.CITY)
        time.sleep(2)
        acp.enter_state(Data.STATE)
        time.sleep(2)
        acp.enter_zip_code(Data.ZIPCODE)
        time.sleep(2)
        acp.enter_country(Data.COUNTRY)
        time.sleep(2)

    # Buttons Page
    def test_formy_buttons(self):
        bp = Formy_Page(self.driver)
        bp.select_buttons()
        time.sleep(2)
        bp.select_primary()
        time.sleep(2)
        bp.select_success()
        time.sleep(2)
        bp.select_info()
        time.sleep(2)
        bp.select_warning()
        time.sleep(2)
        bp.select_danger()
        time.sleep(2)
        bp.select_link()
        time.sleep(2)
        bp.select_left()
        time.sleep(2)
        bp.select_middle()
        time.sleep(2)
        bp.select_right()
        time.sleep(2)
        bp.select_1button()
        time.sleep(2)
        bp.select_2button()
        time.sleep(2)
        bp.select_dropdown()
        time.sleep(2)
        bp.select_dropdown_link1()
        time.sleep(2)
        bp.select_dropdown()
        time.sleep(2)
        bp.select_dropdown_link2()
        time.sleep(2)

    # CheckBox
    def test_formy_checkbox(self):
        cbp = Formy_Page(self.driver)
        cbp.select_checkbox()
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox1_checkbox_selected()}")
        cbp.select_checkbox1()
        print(f"Should: True ==== {cbp.is_checkbox1_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox2_checkbox_selected()}")
        cbp.select_checkbox2()
        print(f"Should: True ==== {cbp.is_checkbox2_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox3_checkbox_selected()}")
        cbp.select_checkbox3()
        print(f"Should: True ==== {cbp.is_checkbox3_checkbox_selected()}")
        time.sleep(2)

    # Date Picker
    def test_formy_datepicker(self):
        dp = Formy_Page(self.driver)
        dp.select_datepicker()
        time.sleep(2)
        dp.select_datepicker_textbox()
        time.sleep(2)
        dp.select_current_date()
        time.sleep(2)

    # Drag and Drop
    def test_drag_and_drop(self):
        dd = Formy_Page(self.driver)
        time.sleep(2)
        dd.click_drag_and_drop_button()
        time.sleep(2)
        # dd.switch_to_iframe_for_drag_and_drop()
        time.sleep(2)
        dd.drag_and_drop()
        time.sleep(5)

    @pytest.mark.sanity# Dropdown
    def test_dropdown(self):
        dp = Formy_Page(self.driver)
        time.sleep(2)
        dp.select_dropdown1()
        time.sleep(5)

    # Enable and Disable
    def test_check_enabled_disable(self):
        ed = Formy_Page(self.driver)
        ed.click_on_enable_disable_button()
        assert ed.check_is_disabled() == False
        assert ed.check_is_enabled() == True

    # File Upload
    def test_file_upload(self):
        ful = Formy_Page(self.driver)
        time.sleep(2)
        ful.click_file_upload()
        time.sleep(2)
        ful.upload_photo()
        time.sleep(3)

    # Keyboard and Mouse Press
    def test_key_press(self):
        kp = Formy_Page(self.driver)
        kp.click_on_key_and_mouse_press()
        kp.enter_full_name()
        time.sleep(2)
        kp.select_all_text()
        time.sleep(1)
        kp.delete_from_keyboard()
        time.sleep(1)
        kp.click_button_by_mouse()
        time.sleep(5)

    # Modal
    def test_modal(self):
        md = Formy_Page(self.driver)
        md.click_on_modal_button()
        time.sleep(1)
        md.click_on_open_modal_button()
        time.sleep(2)
        md.click_on_ok_button()
        time.sleep(2)
        md.click_on_close_button()
        time.sleep(2)

    # Page Scroll
    def test_page_scroll(self):
        ps = Formy_Page(self.driver)
        time.sleep(3)
        ps.click_on_page_scroll()
        time.sleep(3)
        # ps.scroll_into_view()
        # time.sleep(2)
        ps.scroll_into_bottom()
        ps.enter_full_name_scroll(Data.FULL_NAME_SCROLL)
        time.sleep(2)
        ps.enter_date(Data.DATE)

    # Radio Button
    def test_radio_button(self):
        rb = Formy_Page(self.driver)
        time.sleep(2)
        rb.select_radio_button()
        time.sleep(4)
        print(f" Should: False------>{rb.is_radio_button1_selected()}")
        rb.select_radio_button1()
        print(f"Should: True--------->{rb.is_radio_button1_selected()}")
        time.sleep(5)
        print(f" Should: False------>{rb.is_radio_button2_selected()}")
        rb.select_radio_button2()
        print(f"Should: True--------->{rb.is_radio_button2_selected()}")
        time.sleep(5)
        print(f" Should: False------>{rb.is_radio_button3_selected()}")
        rb.select_radio_button3()
        print(f"Should: True--------->{rb.is_radio_button3_selected()}")
        time.sleep(5)

    # Switch Window
    def test_switch_window(self):
        wd = Formy_Page(self.driver)
        wd.click_on_switch_window_button()
        wd.click_on_open_new_tab()
        time.sleep(2)
        wd.click_on_switch_window_button()
        wd.click_on_alert_button()
        time.sleep(2)
        wd.switch_to_alert()
        time.sleep(5)

    # Complete Web Form
    def test_complete_web_form(self):
        cwf = Formy_Page(self.driver)
        time.sleep(2)
        cwf.select_complete_web_form()
        time.sleep(2)
        cwf.enter_first_name(Data.First_name)
        time.sleep(2)
        cwf.enter_last_name(Data.Last_name)
        time.sleep(2)
        cwf.enter_job_title(Data.Job_title)
        time.sleep(2)
        # Checkbox
        print(f" Should: False------>{cwf.is_high_school_selected()}")
        cwf.select_high_school()
        print(f"Should: True--------->{cwf.is_high_school_selected()}")
        time.sleep(5)
        print(f" Should: False------>{cwf.is_college_selected()}")
        cwf.select_college()
        print(f"Should: True--------->{cwf.is_college_selected()}")
        time.sleep(5)
        print(f" Should: False------>{cwf.is_grad_school_selected()}")
        cwf.select_grad_school()
        print(f"Should: True--------->{cwf.is_grad_school_selected()}")
        time.sleep(5)
        # Radio Button
        print(f"Should: False ==== {cwf.is_male_checkbox_selected()}")
        cwf.select_male_checkbox()
        print(f"Should: True ==== {cwf.is_male_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cwf.is_female_checkbox_selected()}")
        cwf.select_female_checkbox()
        print(f"Should: True ==== {cwf.is_female_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cwf.is_prefer_checkbox_selected()}")
        cwf.select_prefer_checkbox()
        print(f"Should: True ==== {cwf.is_prefer_checkbox_selected()}")
        time.sleep(2)
        cwf.select_year_of_experience()
        time.sleep(2)
        cwf.select_datepicker_textbox1()
        time.sleep(2)
        cwf.select_current_date1()
        time.sleep(2)
        cwf.select_submit_button()
        time.sleep(2)
