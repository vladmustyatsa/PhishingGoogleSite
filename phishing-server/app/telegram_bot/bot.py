from telebot import TeleBot, types
from time import sleep
from flask import request
from loguru import logger
from app import app

TOKEN = app.config['TELEBOT_TOKEN']
PROXI_HOST = app.config['PROXI_HOST']

bot = TeleBot(TOKEN)
bot.remove_webhook()
sleep(1)
bot.set_webhook(f'https://{PROXI_HOST}/telebot/{TOKEN}')

from .handlers import *

@app.route(f"/telebot/{app.config['TELEBOT_TOKEN']}", methods=['POST'])
def handle_requests_to_bot():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


