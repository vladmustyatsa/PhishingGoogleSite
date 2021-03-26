import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
sio = SocketIO(app)

if __name__ == "__main__":
    sio.run(app)