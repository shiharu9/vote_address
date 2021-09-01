from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=40)
    house = models.CharField(max_length=10)
    residents = models.IntegerField(default=0)
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Address, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
