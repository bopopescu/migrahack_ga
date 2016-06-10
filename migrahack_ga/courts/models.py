from __future__ import unicode_literals

from django.db import models


class Court(models.Model):
    name     = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    state    = models.CharField(max_length=20)


class Asylum(models.Model):
    court      = models.ForeignKey(Court, null=True)
    year       = models.IntegerField()
    grants     = models.IntegerField()
    denials    = models.IntegerField()
    grant_rate = models.FloatField()


class Detainers(models.Model):
    state = models.CharField(max_length=20)
    year  = models.IntegerField()
    detainer_count = models.IntegerField()

class Judge(models.Model):
    name     = models.CharField(max_length=50)
    court    = models.ForeignKey(Court, null=True)


class Case(models.Model):
    case_no  = models.CharField(max_length=100)
    court    = models.ForeignKey(Court, null=True)
    judge    = models.ForeignKey(Judge, null=True)


class Individual(models.Model):
    name = models.CharField(max_length=50)
    case = models.ForeignKey(Case,null=True)


# Create your models here.
