import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('login data', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('login data', 'useremail')
        return email

    @staticmethod
    def getPassword():
        password = config.get('login data', 'password')
        return password

    @staticmethod
    def firstName():
        firstname = config.get('Profile data', 'firstname')
        return firstname

    @staticmethod
    def lastName():
        lastName = config.get('Profile data', 'lastname')
        return lastName

    @staticmethod
    def phonenumber():
        phonenumber = config.get('Profile data', 'phonenumber')
        return phonenumber

    @staticmethod
    def userfirstname():
        userfirstname = config.get('User Data', 'userfirstname')
        return userfirstname

    @staticmethod
    def userlastname():
        userlastname = config.get('User Data', 'userlastname')
        return userlastname

    @staticmethod
    def useremail():
        useremail = config.get('User Data', 'useremail')
        return useremail

    @staticmethod
    def useraddress():
        useraddress = config.get('User Data', 'address')
        return useraddress
