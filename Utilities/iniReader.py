import configparser

config = configparser.RawConfigParser()
config.read('..\\OrangeHrm\\configuration\\config.ini')


class ReadIni:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        print('so the url is :', url)
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
