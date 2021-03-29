from app import app


if __name__ == "__main__":
    from app import sio
    from loguru import logger
    logger.info('SERVER STARTED')
    sio.run(app)