from django.db import models

# Create your models here.

class EnteredQueries(models.Model):
    entered_text = models.CharField(max_length=200)

    def __str__(self):
        return self.entered_text
