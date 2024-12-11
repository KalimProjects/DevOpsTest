from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title