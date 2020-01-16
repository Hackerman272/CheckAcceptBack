from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# from django.db import models
#
# class Sue(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     middle_name = models.CharField(max_length=200)
#     address_street = models.CharField(max_length=200)
#     address_house = models.CharField(max_length=200)
#     company = models.CharField(max_length=200)
#     children = models.CharField(max_length=200)
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)