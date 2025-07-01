from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    text_name_id = "name"
    text_confirm_password_id = "password-confirm"


    def Enter_Name(self, name):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.text_name_id)))
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def Enter_Confirm_Password(self, confirm_password):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(confirm_password)