from flask import request
from flask_socketio import SocketIO
from app import app
from loguru import logger

sio = SocketIO(app, cors_allowed_origins='*')

@sio.on('connect')
def connect():
    logger.info(f'[{request.sid}] connected')
