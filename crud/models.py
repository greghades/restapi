from django.db import models
from django.contrib.auth.models import User

PRIORITIES = (
    ("HIGH", "HIGH"),
    ("MEDIUM", "MEDIUM"),
    ("LOW", "LOW")
)

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date_limited = models.DateField(null=True)
    asignado_a= models.ForeignKey(User,on_delete=models.CASCADE)
    prioridad= models.CharField(choices=PRIORITIES, max_length=20)
    
    
    def __str__(self):
        return self.title
        
