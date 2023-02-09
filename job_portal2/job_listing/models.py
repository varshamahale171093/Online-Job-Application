from django.db import models

# Create your models here.
class JobDB(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)    
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.title}"