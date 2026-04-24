from django.db import models

class Boxer(models.Model):
    fullname=models.CharField(max_length=255)
    hp=models.IntegerField()
    strongest_attack=models.CharField(max_length=255, default='cross')

    def __str__(self):
        return f"This is the representation, and boxer's name is {self.fullname}"
