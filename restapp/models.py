from django.db import models


# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=2500)
    completed=models.BooleanField()
    created_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="images",default="Image/None/Noimg.jpg")
    
    
    def __str__(self):
        return self.name