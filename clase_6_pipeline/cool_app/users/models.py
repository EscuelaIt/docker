from django.db import models


class UserProfile(models.Model):
    bio = models.CharField(max_length=500)
