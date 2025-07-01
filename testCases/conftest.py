import pytest
from selenium import webdriver


@pytest.fixture # decorator
def demo_fixture(): # function
    print("\nThis is demo fixture, this will run first, before testcase") # Code # function body/ block
    # if you are using this fixture in any testcase then it will run before that testcase
    yield # after running the testcase this will run
    print("\nThis is demo fixture, this will run after testcase")


    '''
    browser open--> before testcase
    browser close--> after testcase
    '''

# @pytest.fixture
# def driver_setup():
#     print("\nBrowser opened")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#     print("\nBrowser closed")


'''
pytest_addoption -- > hook up function --> extending pytest framework
Python adoption function is used to pass the command line arguments to pytest
here we are going to add "--browser" command line argument, which is user defined or custom argument.
( -v, -s, -m, -n --> predefined arguments) 
'''


def pytest_addoption(parser):
    parser.addoption("--browser")
# here we are going to add "--browser" command line argument, which is user defined or custom argument.

# --browser chrome
# --browser firefox
# --browser edge


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
         print("launching chrome headless browser")
         chrome_options = webdriver.ChromeOptions()
         chrome_options.add_argument("--headless")
         driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()
        # print("launching chrome headless browser")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # attaching driver to class
    request.cls.driver = driver
    yield driver
    print("\nBrowser closed")
    driver.quit()


def pytest_metadata(metadata):
    # To add metadata
    metadata["Project Name"] = "CredKart"
    metadata["Module Name"] = "Login"
    metadata["Tester Name"] = "Credence"
    metadata["URL"] = "https://apps.credence.in/"
    # To remove metadata
    del metadata["Platform"]

    # edit summary in html report --> your task

@pytest.fixture(params=[
    ("credencejune01@credence.in", "Credence@123", "Pass"),
    ("credencejune01@credence.in1", "Credence@123", "Fail"),
    ("credencejune01@credence.in", "Credence@1231", "Fail"),
    ("credencejune01@credence.in1", "Credence@1231", "Fail")
])
def get_data_for_login(request): # function with parameter
    return request.param

