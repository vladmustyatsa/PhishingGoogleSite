import os


class DevelopmentConfig:
    DEBUG = True
    TELEBOT_TOKEN = os.environ["TELEBOT_TOKEN"]
    PROXI_HOST = os.environ['PROXI_HOST']
