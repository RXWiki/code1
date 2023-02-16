from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.urls import reverse


class Questions(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_right = models.BooleanField(default=False)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('questions', kwargs={'quest': self.pk})


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_text2 = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Person(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    resultat = models.IntegerField(default=0)


    def __str__(self):
        return self.borrower
