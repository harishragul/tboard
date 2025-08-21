from django.db import models
from teams.models import Member, Organization
from django.utils import timezone

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization, default=None, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    task = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(default=None, null=True)
    assigned_to = models.ForeignKey(Member, related_name="assigned_to", default=None, null=True, on_delete=models.SET_NULL)
    assigned_by = models.ForeignKey(Member, related_name="assigned_by", default=None, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, default=None, null=True, on_delete=models.SET_NULL)
    total_effort = models.IntegerField(default=None, null=True)
    acutal_effort = models.IntegerField(default=None, null=True)
    remaining_effort = models.IntegerField(default=None, null=True)
    due = models.DateTimeField(default=None)
    organization = models.ForeignKey(Organization, default=None, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.task}"