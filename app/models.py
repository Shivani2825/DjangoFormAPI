from django.db import models

class StudentData(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    password= models.CharField(max_length=150)
    rpassword= models.CharField(max_length=150, default='None')


    def __str__(self):
        return self.name
    
