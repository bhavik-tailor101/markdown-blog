from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=250)
    text = models.TextField(null=False)

class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    text = models.TextField(null=False)