import logging
import time

import sys

from selenium.webdriver.common.by import By

sys.path.append('/home/tanushree/Downloads/cQube_v5/')
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.nishtha import nishtha
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    homepage = None
    nishtha = None
    driver = None
    GetData = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(30)
        cls.homepage = Homepage(cls.driver)
        cls.nishtha = nishtha(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.homepage.test_click_on_state_button()
        cls.nishtha.click_on_access_nishtha_menu()
        cls.logger = CustomLogger.setup_logger('nishtha', ReadConfig.get_logs_directory() + "/Dashboard.log",
                                               level=logging.DEBUG)

    '''This Test script checking the navigation is happening or not '''

    def test_check_navigation_to_nishtha(self):
        self.logger.info("*************** Tc_cQube Testing Started *****************")
        time.sleep(2)
        if 'nishtha' in self.driver.current_url and 'NISHTHA' in self.driver.page_source:
            self.logger.info("******************* nas Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("***************nas Dashboard Button is not Working ******************")
            assert False
        self.nishtha.click_menu()
        self.logger.info("*************** Tc_cQube Testing Ended *****************")

    '''Test Scripts to Click on the Implementation Tab '''

    def test_click_on_the_implementation_status_tab_button(self):
        self.logger.info("*************** Tc_cQube Testing started *****************")
        self.driver.find_element(By.XPATH, self.nishtha.implementation_tab_status).click()
        time.sleep(3)
        Implementation_status = self.nishtha.click_implementation_status()
        time.sleep(3)
        if "true" == Implementation_status:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube Testing ended *****************")

    '''This Test script checking the A- Button '''

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing Started *****************")
        res = self.nishtha.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing completed *****************")

    '''This Test script checking home button '''

    def test_home_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing ended *****************")

    '''This Test script checking full screen button is working or not'''

    def test_implementation_full_screen(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        self.nishtha.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing ended *****************")

    '''Test Script to Validate the Nishtha - Enrolment Metric Card'''

    def test_validate_Total_Enrolment_metrics(self):
        self.logger.info("*************** Testing started *****************")
        time.sleep(5)
        self.nishtha.click_implementation_status()
        time.sleep(5)
        card_value = self.nishtha.get_total_Enrolment_value()
        card_title = self.nishtha.get_total_Enrolment_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False

    '''Test Script to Validate the Nishtha - total completion metrics Card'''

    def test_validate_Total_Completion_metrics(self):
        self.logger.info("*************** Testing started *****************")
        time.sleep(5)
        self.nishtha.click_implementation_status()
        time.sleep(5)
        card_value = self.nishtha.get_total_completion_value()
        card_title = self.nishtha.get_total_completion_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False

    '''Test Script to Validate the Nishtha - Total_Certification Card'''

    def test_validate_Total_Certification_metrics(self):
        self.logger.info("*************** Testing started *****************")
        time.sleep(5)
        self.nishtha.click_implementation_status()
        time.sleep(5)
        card_value = self.nishtha.get_total_Certification_value()
        card_title = self.nishtha.get_total_Certification_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False

    '''Test Script to Validate the Nishtha - Total mediums Card'''

    def test_validate_Total_mediums_metrics(self):
        self.logger.info("*************** Testing started *****************")
        time.sleep(5)
        self.nishtha.click_implementation_status()
        time.sleep(5)
        card_value = self.nishtha.get_total_Mediums_value()
        card_title = self.nishtha.get_total_Mediums_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False

    '''Test Scripts to Click on the table Header and validate sorting functionality'''

    def test_click_the_table_headers_validate_sorting(self):
        self.logger.info("**************** Tc_cQube_Nishtha_018 is Started ... *************** ")
        # self.nishtha.click_on_implementation_tab()
        self.nishtha.click_implementation_status()
        result = self.nishtha.check_table_program_headers_clickable()
        if result == 0:
            self.logger.info("********** program sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("***************** program sorting functionality is not working  ...**************")
            assert False
        result = self.nishtha.test_check_nishtha_started_headers_clickable()
        if result == 0:
            self.logger.info("********** nishtha started sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("*********** nishtha started sorting functionality is not working  ********")
            assert False
        self.logger.info("**************** Tc_cQube_Nishtha_018 is Ended ... *************** ")

    '''This Test script checking logout button is working or not'''

    def test_click_implemenatation_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        time.sleep(2)
        self.nishtha.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  course and medium page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** course and medium Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")



# ===========================================================================================================

    '''Test Scripts to Click on the Course and medium status Tab '''

    def test_click_on_the_course_and_medium_status_tab_button(self):
        self.logger.info("*************** Tc_cQube Testing started *****************")
        # self.nishtha.click_on_course_and_medium_tab()
        # course_and_medium_status = self.nishtha.click_course_and_medium_status1()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, self.nishtha.course_medium_tab_status).click()
        time.sleep(3)
        course_and_medium_status = self.nishtha.click_course_and_medium_status()
        if "true" == course_and_medium_status:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube Testing ended *****************")

    '''Test Scripts to Click on the table Header and validate sorting functionality'''

    def test_click_the_course_and_medium_table_headers_validate_sorting(self):
        self.logger.info("**************** Tc_cQube_Nishtha_018 is Started  *************** ")
        # self.nishtha.click_on_course_and_medium_tab()
        self.driver.find_element(By.XPATH, self.nishtha.course_medium_tab_status).click()
        time.sleep(3)
        course_and_medium_status = self.nishtha.click_course_and_medium_status()
        if "true" == course_and_medium_status:
            self.logger.info("*********** Tab is selecting *l**************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        result = self.nishtha.check_table_program_headers_clickable()
        time.sleep(2)
        if result == 0:
            self.logger.info("********** program header sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("***************** program header sorting functionality is not working  ...**************")
            assert False
        result = self.nishtha.test_check_course_table_values()
        if result == 0:
            self.logger.info("********** Course Header sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("***************** Course Header sorting functionality is not working  ...**************")
            assert False
        result = self.nishtha.test_check_medium_table_values()
        if result == 0:
            self.logger.info("********** Medium Header sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("***************** Medium Header sorting functionality is not working  ...**************")
            assert False

        self.logger.info("**************** Tc_cQube_Nishtha_018 is Ended ... *************** ")

    '''This Test script checking the A- Button '''

    def test_course_and_medium_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing Started *****************")
        res = self.nishtha.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_course_and_medium_status_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_course_and_medium_status_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing completed *****************")

    '''This Test script checking home button '''

    def test_course_wise_home_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing ended *****************")

    '''This Test script checking full screen button is working or not'''

    def test_course_wise_full_screen(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        self.nishtha.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing ended *****************")

    '''This Test script checking logout button is working or not'''

    def test_click_course_and_medium_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        time.sleep(2)
        self.nishtha.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  course and medium page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** course and medium Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")


# ====================================================================================================

    '''Test Scripts to Click on the percent against potential base Tab '''

    def test_click_on_the_against_potential_base_tab_button(self):
        self.logger.info("*************** Tc_cQube Testing started *****************")
        self.driver.find_element(By.XPATH, self.nishtha.potential_tab_status).click()
        time.sleep(3)
        per_against_potential_base = self.nishtha.click_per_against_potential_base()
        if "true" == per_against_potential_base:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube Testing ended *****************")

    '''This Test script checking the A- Button '''

    def test_against_potential_base_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing Started *****************")
        res = self.nishtha.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_against_potential_base_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_against_potential_base_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing completed *****************")

    '''This Test script checking home button '''

    def test_potential_home_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing ended *****************")

    '''This Test script checking full screen button is working or not'''

    def test_potential_full_screen(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        self.nishtha.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing ended *****************")

    '''This Test script checking the stacked bar chart validation '''

    def test_course_program_wise_stacked_bar_chart_validations(self):
        self.logger.info("**************** Tc_cQube_Nishtha_026 is Started ... *************** ")
        self.driver.find_element(By.XPATH, self.nishtha.potential_tab_status).click()
        time.sleep(3)
        per_against_potential_base = self.nishtha.click_per_against_potential_base()
        if "true" == per_against_potential_base:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        result = self.nishtha.get_course_wise_stacked_bar_tooltip_validation()
        print(result)
        if result == 0:
            self.logger.info("********** Checked potential Stacked Bar ******************")
            assert True
        else:
            self.logger.error("***************** potential Stacked Bar is not showing chart **************")
            assert False
        self.logger.info("**************** Tc_cQube_Nishtha_026 is Ended ... ***************")

    '''This Test script checking logout button is working or not'''

    def test_click_per_against_potential_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        time.sleep(2)
        self.nishtha.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  district officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** district officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")



# ===============================================================================================

    '''Test Scripts to Click on the course wise status Tab '''

    def test_click_on_the_course_wise_status_tab_button(self):
        self.logger.info("*************** Tc_cQube Testing started *****************")
        self.driver.find_element(By.XPATH, self.nishtha.course_wise_tab_status).click()
        time.sleep(3)
        course_wise_status = self.nishtha.click_course_wise_status()
        if "true" == course_wise_status:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube Testing ended *****************")

    '''This Test script checking the A-  Button '''

    def test_course_wise_status_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing Started *****************")
        res = self.nishtha.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_course_wise_status_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_course_wise_status_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Started *****************")
        res = self.nishtha.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing completed *****************")

    '''This Test script checking the stacked bar chart validation '''

    def test_course_wise_stacked_bar_chart_validations(self):
        self.logger.info("**************** Tc_cQube_Nishtha_027 is Started ... *************** ")
        self.driver.find_element(By.XPATH, self.nishtha.course_wise_tab_status).click()
        time.sleep(3)
        course_wise_status = self.nishtha.click_course_wise_status()
        if "true" == course_wise_status:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        result = self.nishtha.get_course_wise_stacked_bar_tooltip_validation()
        if result == 0:
            self.logger.info("********** Checked course wise Stacked Bar ******************")
            assert True
        else:
            self.logger.error("***************** course Wise Stacked Bar is not showing chart **************")
            assert False
        self.logger.info("**************** Tc_cQube_Nishtha_027 is Ended ... ***************")

    '''This Test script checking home button is working or not'''

    def test_course_home_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing ended *****************")

    '''This Test script checking logout button is working or not'''

    def test_click_course_wise_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        time.sleep(2)
        # self.nishtha.course_wise_tab_status()
        self.nishtha.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  district officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** district officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    '''This Test script checking full screen button is working or not'''

    def test_full_screen(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        self.nishtha.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing ended *****************")

























