import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import log_generator_class
from utilities.ReadConfig import ReadConfigClass
from utilities import Excel_Utils


@pytest.mark.usefixtures("driver_setup")
class Test_Login_Excel_003:
    log = log_generator_class.loggen_method()
    login_url = ReadConfigClass.get_data_for_login_url()
    excel_path = r"F:\Automation testing\4.Credkart_Pytest_Framework\TestData\Test_Data.xlsx"
    sheet_name = "login_data"

    def test_CredKart_Login_Excel_003(self, driver_setup): # Injecting driver from fixture
        driver = driver_setup
        self.log.info("Testcase test_CredKart_Login_Excel_003 is started")
        lp = Login_Page_Class(driver)
        self.log.info("Reading the data from excel file")
        rows = Excel_Utils.get_row_count(self.excel_path, self.sheet_name)
        self.log.info("Number of rows in excel file is: %d", rows)

        result_list = []

        for i in range(2, rows + 1):
            self.log.info(f"Opening browser and landing on login page -- {self.login_url}")
            driver.get(self.login_url)

            email = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 2)
            password = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 3)
            expected_result = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 4)

            self.log.info(f"Entering email: {email}")
            lp.Enter_Email(email)
            self.log.info("Entering password")
            lp.Enter_Password(password)
            self.log.info("Clicking on login button")
            lp.Click_Submit_Button()

            self.log.info("Verifying user login")
            if lp.verify_menu() == "Pass":
                self.log.info("User logged in successfully")
                Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 5, "Pass")
                driver.save_screenshot(f".\\Screenshots\\test_CredKart_Login_Excel_003_{i}_{email}_pass.png")
                lp.Click_Menu_Button()
                lp.Click_Logout_Link()
                actual_result = "Pass"
            else:
                self.log.info("User not logged in")
                Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 5, "Fail")
                driver.save_screenshot(f".\\Screenshots\\test_CredKart_Login_Excel_003_{i}_{email}_fail.png")
                actual_result = "Fail"

            test_case_status = "Pass" if expected_result == actual_result else "Fail"
            result_list.append(test_case_status)
            Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 6, test_case_status)

        if "Fail" not in result_list:
            self.log.info("All the test cases passed")
            assert True
        else:
            self.log.info("Some test cases failed")
            assert False

        self.log.info("Testcase test_CredKart_Login_Excel_003 is completed")
