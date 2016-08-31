from django.db import models

SITES = (
    ('g', 'Google'),
    ('y', 'Yandex'),
    ('i', 'Instagram'),
)


class Tasks(models.Model):
    query = models.CharField(max_length=300)
    scrapyd_response = models.TextField(blank=True)

    def __str__(self):
        return self.query


class Results(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    direct_link = models.URLField(max_length=500)
    source_link = models.URLField(max_length=500)
    rank = models.PositiveSmallIntegerField()
    site = models.CharField(max_length=1, choices=SITES)

    def __str__(self):
        return self.task
