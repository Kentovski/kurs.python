import logging

from django.db import models
from django.contrib.auth.models import User

LOG_LEVEL = (
    (logging.INFO, 'info'),
    (logging.WARNING, 'warning'),
    (logging.DEBUG, 'debug'),
    (logging.ERROR, 'error'),
    (logging.FATAL, 'fatal'),
)


class Log(models.Model):
    time = models.DateTimeField(blank=True)
    level = models.PositiveIntegerField(choices=LOG_LEVEL, default=logging.ERROR, blank=True)
    message = models.TextField(blank=True)
    sender = models.ForeignKey(User)

    def __str__(self):
        return '{} {}'.format(self.sender, self.time)
