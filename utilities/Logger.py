import logging

class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger()
        log_file = logging.FileHandler(r"F:\Automation testing\4.Credkart_Pytest_Framework\Logs\Credkart_Automation.Log")
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s  - %(lineno)d - %(message)s") #
        log_file.setFormatter(log_format) # here we are setting log format
        logger.addHandler(log_file) # here we are adding log file
        logger.setLevel(logging.DEBUG) # here we are setting log level
        return logger
