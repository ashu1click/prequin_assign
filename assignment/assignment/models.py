from django.db import models

class Array(models.Model):
    sentence = models.CharField(max_length=600)

    