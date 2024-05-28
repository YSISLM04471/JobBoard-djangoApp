from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    company = models.CharField(max_length=50)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)