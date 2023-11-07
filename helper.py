class Converter:
    @classmethod
    def convert(self, message):
        pass

class BotException(Exception):
    pass

class IncorrectMessage(BotException):
    pass

