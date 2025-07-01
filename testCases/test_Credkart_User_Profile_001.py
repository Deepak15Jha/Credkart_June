import sys
import os
import time

import allure
import pytest



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from faker import Faker
from pageObjects.Registration_Page import Registration_Page_Class
from pageObjects.Login_Page import Login_Page_Class
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()
    log = log_generator_class.loggen_method()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("CredKart login")
    @allure.story("story: CredKart Login")
    @allure.description("This test case is to validate Credkart Title functionality")
    @allure.issue("issue : https://credence.in/")
    @allure.link("https://credence.in/")
    @allure.testcase("https://credence.in/")
    @allure.epic("Epic : CredKart")
    @allure.sub_suite("CredKart Login")
    @allure.title("test_CredKart_Title_001")
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.dependency(name ="test_CredKart_Title_001")
    @pytest.mark.smoke
    @pytest.mark.web
    def test_CredKart_Title_001(self):
        self.log.info("Testcase test_CredKart_Title_001 is started")
        self.log.info(f"Opening browser and landing on login page--{self.login_url}")
        self.driver.get(self.login_url)
        self.driver.maximize_window()
        # self.log.debug("This is info")
        # self.log.info("This is info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")

        self.log.info("Checking title of login page")
        if self.driver.title == "CredKart":
            self.log.info("Landed on correct page and it's title is: " + self.driver.title)
            #print("you are landed on correct page and it's title is:", self.driver.title)
            self.driver.save_screenshot(
                r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Successfully.png"
                )
            allure.attach.file(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Successfully.png", name="User login Successfully", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.info("Landed on incorrect page and it's title is: " + self.driver.title)
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Failed.png")
            allure.attach.file(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Failed.png", name="User login Failed", attachment_type=allure.attachment_type.PNG)
            #print("you are landed on wrong page and it's title is:", self.driver.title)
            assert False
        self.log.info("Testcase test_CredKart_Title_001 is completed\n")


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
    @pytest.mark.dependency(depends=["test_CredKart_Title_001"])
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.sanity
    @pytest.mark.web
    def test_CredKart_Login_002(self):
        self.log.info("Testcase test_CredKart_Login_002 is started")
        self.log.info(f"Opening browser and landing on login page--{self.login_url}")
        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver) # Object Creation

    #     # Field - Email
    #     email_field = self.driver.find_element(By.ID, "email")
    #     email_field.send_keys(f"Credencejune{value}@credence.in")
        self.log.info(f"Entering email--{self.email}")
        self.lp.Enter_Email(self.email) # hard coding

    #
    #     # Field - Password
    #     password_field = self.driver.find_element(By.ID, "password")
    #     password_field.send_keys("Credence@123")
        self.log.info(f"Entering password")
        self.lp.Enter_Password(self.password) # hard coding

    #
    #     # Button - Login Now
    #     login_now_button = self.driver.find_element(By.CLASS_NAME, "btn")
    #     login_now_button.click()
        self.log.info("Clicking on login button")
        self.lp.Click_Submit_Button()

    #
    #     # Verify the User login Successfully
    #     wait = WebDriverWait(self.driver, 5)
    #     try:
    #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
    #         self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
    #         print("User login Successfully")
    #         #self.driver.save_screenshot("User login Successfully.png")
    #     except:
    #         print("User login Failed")
    #         #self.driver.save_screenshot("User login Failed.png")
    # else:
    #     print("you are landed on wrong page and it's title is:", self.driver.title)
        self.log.info("Verifying user login")
        if self.lp.verify_menu() == "Pass":
            self.log.info("user Login Successfully")
            #self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Link()
            assert True
        else:
            self.log.info("user Login Failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User login Failed.png")
            assert False
        self.log.info("Testcase test_CredKart_Login_002 is completed\n")


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("CredKart login")
    @allure.story("story: CredKart Login")
    @allure.description("This test case is to validate Credkart Registration functionality")
    @allure.issue("issue : https://credence.in/")
    @allure.link("https://credence.in/")
    @allure.testcase("https://credence.in/")
    @allure.epic("Epic : CredKart")
    @allure.sub_suite("CredKart Login")
    @allure.title("test_CredKart_Registration_003")
    @pytest.mark.dependency(depends=["test_CredKart_Title_001"])
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.web
    def test_CredKart_Registration_003(self):
        self.log.info("Testcase test_CredKart_Registration_003 is started")
        self.log.info(f"Opening browser and landing on login page--{self.register_url}")
        self.driver.get(self.register_url)
        self.rp = Registration_Page_Class(self.driver) # Object Creation
        name = Faker().name()
        email = Faker().email()
        print(f"Name: {name}, Email: {email}")
        # Field - Name
        self.log.info(f"Entering name--{name}")
        self.rp.Enter_Name(name)

        # Field - Email
        self.log.info(f"Entering email--{email}")
        self.rp.Enter_Email(email)

        # Field - Password
        self.log.info(f"Entering password")
        self.rp.Enter_Password("Credence@123")

        # Field - Confirm Password
        self.log.info(f"Entering confirm password")
        self.rp.Enter_Confirm_Password("Credence@123")

        # Button - Submit
        self.log.info("Clicking on registration button")
        self.rp.Click_Submit_Button() # registration button

        # Verify Registration Successfully
        self.log.info("Verifying user registration")
        if self.rp.verify_menu() == "Pass":
            self.log.info("user Registration Successfully")
            # self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            self.log.info("Clicking on menu button")
            self.rp.Click_Menu_Button()
            self.log.info("Clicking on logout link")
            self.rp.Click_Logout_Link()
            assert True
        else:
            self.log.info("user Registration Failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(r"F:\Automation testing\4.Credkart_Pytest_Framework\Screenshots\User Registration Failed.png")
            assert False
        self.log.info("Testcase test_CredKart_Registration_003 is completed\n")


# added registration
# common value--> config.ini
# driver_setup implemented at class level
# driver_setup, driver attached to class
# logger class, and method


# log
# rerun failed testcases
# allure report
# params, excel
# add test cases


# jenkins
# git


'''
To create dependency between test cases :
1. pip install pytest-dependency
2. add decorator @pytest.mark.dependency, for testcase on which other test case depends
3. add decorator @pytest.mark.dependency(depends=["test_CredKart_Title_001"]), for testcase to which test case depends


'''

'''
1. To generate html report
pytest -v  -n auto --html=HTMLReports/My_Report.html 

2. To generate Allure report files
pytest -v  -n auto --alluredir=AllureReports

3. To generate Allure report
allure serve AllureReports
'''