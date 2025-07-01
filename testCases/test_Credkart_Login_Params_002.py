import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import allure
import pytest
from faker import Faker
from pageObjects.Registration_Page import Registration_Page_Class
from pageObjects.Login_Page import Login_Page_Class
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()
    log = log_generator_class.loggen_method()



    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("CredKart login")
    @allure.story("story: CredKart Login")
    @allure.description("This test case is to validate Credkart Login functionality")
    @allure.issue("issue : https://credence.in/")
    @allure.link("https://credence.in/")
    @allure.testcase("https://credence.in/")
    @allure.epic("Epic : CredKart")
    @allure.sub_suite("CredKart Login")
    @allure.title("test_CredKart_Login_002")
    @pytest.mark.sanity
    @pytest.mark.web
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_CredKart_Login_params_004(self,get_data_for_login):
        self.log.info("Testcase test_CredKart_Login_002 is started")
        self.log.info(f"Opening browser and landing on login page--{self.login_url}")
        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver) # Object Creation

        self.email = get_data_for_login[0]
        self.password = get_data_for_login[1]
        self.expected_result = get_data_for_login[2]

        self.log.info(f"Entering email--{self.email}")
        self.lp.Enter_Email(self.email) # hard coding
        self.log.info(f"Entering password")
        self.lp.Enter_Password(self.password) # hard coding
        self.log.info("Clicking on login button")
        self.lp.Click_Submit_Button()
        self.log.info("Verifying user login")
        if self.lp.verify_menu() == "Pass":
            self.log.info("user Login Successfully")
            #self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Link()
            actual_result = "Pass"
        else:
            self.log.info("user Login Failed")
            actual_result = "Fail"
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Failed.png")


        assert actual_result == self.expected_result, f"Expected Result: {self.expected_result}, Actual Result: {actual_result}"

        self.log.info("Testcase test_CredKart_Login_002 is completed\n")

