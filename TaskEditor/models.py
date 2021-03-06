

# Create your models here.
from django.db import models
from datetime import datetime, timedelta

from django.db.models.fields import BooleanField

# Create your models here.
class ClassList(models.Model) :
    course_num = models.CharField(max_length=6)
    course_name = models.CharField(max_length=30)

    def __str__(self) :
        return (self.course_num)
class AssignmentType(models.Model) :
    assign_type = models.CharField(max_length=15)

    def __str__(self) :
        return (self.assign_type)
class Priority(models.Model) :
    priority = models.CharField(max_length=10)

    def __str__(self) :
        return (self.priority)


class Task(models.Model) :
    course = models.ForeignKey(ClassList, models.CASCADE)
    assignment = models.ForeignKey(AssignmentType, models.CASCADE)
    priority = models.ForeignKey(Priority, models.CASCADE)
    title = models.CharField(max_length=50)
    due_date = models.DateField(default=datetime.today, blank=True)
    completed = models.BooleanField(default=False)
    notes = models.CharField(max_length=50)
    #cost = models.DecimalField(max_digits=8, decimal_places=2)
    #main_photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return (self.title)
