from django.db import models #This line is importing the models module from Django. 
#This module is used to define the data structure required for your application.

# Create your models here.

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)
    
# class React(models.Model):: This line is defining a new model (or data structure) named React. This model inherits from models.Model, which is a base class provided by Django.
# employee = models.CharField(max_length=30): This line is defining a field named employee in the React model. The field is of type CharField, which is a string field. The max_length=30 argument specifies that this field can hold a maximum of 30 characters.
# department = models.CharField(max_length=200): This line is defining another field named department in the React model. This field is also of type CharField, but it can hold a maximum of 200 characters.
# In Django, each attribute of the model class represents a database field. So, the React model will create a database table named React with two columns: employee and department.