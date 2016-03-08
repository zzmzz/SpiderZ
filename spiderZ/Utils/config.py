import ConfigParser

class Config:
    cf = ConfigParser.ConfigParser()
    cf.read("config/config.conf")

    @staticmethod
    def getProperty(domain,name):
        return Config.cf.get(domain,name)
