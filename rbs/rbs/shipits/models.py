from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    score = models.IntegerField()

    class Meta:
        app_label = "rbs"

    def __unicode__(self):
        return self.name
