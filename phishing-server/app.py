import eventlet
eventlet.monkey_patch()
from flask import Flask, request
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
from telegram_bot import bot
from socks.sock import sio

