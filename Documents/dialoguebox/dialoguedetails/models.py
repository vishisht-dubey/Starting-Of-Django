from django.db import models


class DialogueBox(models.Model):
    feedback = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    agree = models.BooleanField(default=False)

