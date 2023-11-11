from django.db import models


class Entry(models.Model):
    user_id = models.CharField(max_length=50)
    value = models.CharField(max_length=10)
