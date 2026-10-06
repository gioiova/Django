from django.db import models

# Create your models here.
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'lecturers'

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    credits =models.PositiveSmallIntegerField(default=5)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True,blank=True)
    
    
    class Meta:
        db_table = 'courses'
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    courses = models.ManyToManyField(Course)
    
    class Meta:
        db_table = 'students'