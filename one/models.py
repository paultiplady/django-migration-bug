from django.db import models


class Rename2(models.Model):
    pass


class Related(models.Model):
    rename1 = models.ForeignKey('one.Rename2')
