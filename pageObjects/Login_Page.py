from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    text_email_id = "email"
    text_password_id = "password"
    button_login_class = "btn"
    click_menu_button_class = "dropdown-toggle"
    click_logout_link_css = "a[href='https://automation.credence.in/logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

# driver is defined in conftest.py

    def Enter_Email(self, email):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.text_email_id)))
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def Click_Submit_Button(self):
        self.driver.find_element(By.CLASS_NAME,self.button_login_class).click()

    def Click_Menu_Button(self):
        self.driver.find_element(By.CLASS_NAME, self.click_menu_button_class).click()

    def Click_Logout_Link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_logout_link_css).click()


    def verify_menu(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, self.click_menu_button_class)))
            return "Pass"
        except:
            return "Fail"