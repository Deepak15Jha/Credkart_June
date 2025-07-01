import configparser

config = configparser.RawConfigParser()
config.read(r"F:\Automation testing\4.Credkart_Pytest_Framework\Configurations\config.ini") # best practice



class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        email = config.get("login data", "email")
        return email # credencejune01@credence.in

    @staticmethod
    def get_data_for_password():
        password = config.get("login data", "password")
        return password

    @staticmethod
    def get_data_for_login_url():
        login_url = config.get("Application URL", "login_url")
        return login_url


    @staticmethod
    def get_data_for_register_url():
        register_url = config.get("Application URL", "registration_url")
        return register_url
