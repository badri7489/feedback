from django.db import models

# Create your models here.

class Feedback(models.Model):

    email = models.EmailField()
    feedback = models.TextField()

    # def __str__(self):
    #     return self.email.split('@')[0]