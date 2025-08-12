from django.db import models
from django.contrib.auth.models import User
from uuid import uuid5
from django.utils import timezone

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField()
    website = models.CharField(max_length=256, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Role(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Member(models.Model):
    member_id = models.UUIDField(uuid5, unique=True, null=False, blank=False, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name}: {self.role}"
