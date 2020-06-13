import datetime

from django.db import models
from django.utils import timezone
from PIL import Image



class Question(models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')


    # ...
    def __str__(self):
        return self.question_text




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Employee(models.Model):
        Emp = models.CharField(max_length=200)
        photo = models.ImageField(upload_to='Employee')
        photo = models.ImageField(upload_to='Employee')


        # ...
        def __str__(self):
            return self.Emp




class Employee_Details (models.Model):
    EmployeeID = models.CharField(max_length=200)
    EmployeeName = models.CharField(max_length=200)
    EmployeeDesignation = models.CharField(max_length=200)
    Group = models.CharField(max_length=200)
    soc = models.CharField(max_length=200)
    moc = models.CharField(max_length=200)
    wow = models.CharField(max_length=200)
    dow = models.CharField(max_length=200)
    ho = models.CharField(max_length=200)
    hi = models.CharField(max_length=200)
    boe = models.CharField(max_length=200)
    bow = models.CharField(max_length=200)
    love = models.CharField(max_length=200)
    ka = models.CharField(max_length=200)
    mano = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    surya = models.CharField(max_length=200)
    lov = models.CharField(max_length=200)
    sathya = models.CharField(max_length=200)


# ...
    def __str__(self):
        return self.EmployeeID

