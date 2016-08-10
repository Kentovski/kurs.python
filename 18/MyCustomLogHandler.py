import logging
import requests
from datetime import datetime


class StarHandler(logging.Handler):
    def __init__(self, url, user, password, *args, **kwargs):
        super(StarHandler, self).__init__(level=logging.DEBUG, *args, **kwargs)
        self.url = url
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user = user
        self.password = password

    def emit(self, record):
        requests.post(self.url, data={
                'time': self.time,
                'password': self.password,
                'username': self.user,
                'level': record.levelno,
                'message': record.msg
            })

if __name__ == "__main__":
    star_handler = StarHandler(url='http://127.0.0.1:8000', user='admin', password='djangoadmin')

    logger = logging.getLogger(__name__)
    logger.addHandler(star_handler)

    logger.error('Что-то пошло не так.')
    logger.error('Ошибочка вышла.')
    logger.critical('Хьюстон, у нас проблемы.')
