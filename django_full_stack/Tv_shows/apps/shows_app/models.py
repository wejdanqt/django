from django.db import models


class shows(models.Model):
    title = models.CharField(max_length=45)
    networks = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    des = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
