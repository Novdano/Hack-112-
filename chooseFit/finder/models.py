from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userData(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    weight = models.IntegerField() #pounds
    heightFeet = models.IntegerField(default = 0) #inches
    timeCommit = models.IntegerField() #hoursPerWeek
    intro = models.TextField(default = "Hi")
    goalChoices = ( ("bulking", "bulking"),
                    ("slimming", "slimming"),
                    ("fitness", "fitness" )
                    )
    goals = models.CharField(max_length = 10, choices =goalChoices, default = "fitness")
    heightInches = models.IntegerField(default = 0)
    profile = models.CharField(max_length = 1000, default = "http://cdn3.denofgeek.us/sites/denofgeekus/files/scarlett_johansson.jpg")
    location = models.CharField(max_length = 500, default = "Carnegie Mellon University")
    city = models.CharField(max_length = 100, default = "Pittsburgh")
    state = models.CharField(max_length = 100, default = "PA")

    def __unicode__(self):
        return self.name