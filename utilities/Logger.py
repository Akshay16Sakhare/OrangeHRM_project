import inspect
import logging

class LogGen():

    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\logs\logfiles.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
# LEVELs:

# Debug
# INFO
# Warning
# Error
# Critical