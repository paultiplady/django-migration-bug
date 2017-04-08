from django.db import models


class Related2(models.Model):
    rename1 = models.ForeignKey('one.Rename1')
