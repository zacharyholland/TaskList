

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
    priority = models.Model(max_length=10)

    def __str__(self) :
        return (self.priority)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
            return '%s %s' % (self.first_name, self.last_name)

    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(User, self).save()

class Task(models.Model) :
    course = models.OneToManyField(ClassList, models.CASCADE)
    assignment = models.OneToMany(AssignmentType, models.CASCADE)
    priority = models.OneToMany(Priority, models.CASCADE)
    user = models.OneToManyField(User, models.CASCADE)
    title = models.CharField(max_length=50)
    due_date = models.DateField(default=datetime.today, blank=True)
    completed = BooleanField(default=False)
    notes = models.CharField(max_length=50)
    #cost = models.DecimalField(max_digits=8, decimal_places=2)
    #main_photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return (self.title)
