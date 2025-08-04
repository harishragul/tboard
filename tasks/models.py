from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=128, null=False, blank=False)
    assigned_to = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.task}"