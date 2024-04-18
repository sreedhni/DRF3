from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    snippet_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=5000, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=ACTIVE)
