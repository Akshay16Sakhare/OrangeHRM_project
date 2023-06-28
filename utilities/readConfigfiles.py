# import configparser
#
# config = configparser.RawConfigParser()
# config.read(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\Configuration\config.ini")
#
# class Readvalues():
#
#     @staticmethod
#     def getUsername():
#         username = config.get('login info', 'username')
#         return username
#
#     @staticmethod
#     def getPassword():
#         password = config.get('login info', 'password')
#         return password

import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\Configuration\config.ini")

class Read_values():

    @staticmethod
    def getUser():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPasswrd():
        password = config.get('login info', 'password')
        return password

