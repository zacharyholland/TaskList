from django.contrib import admin
from .models import ClassList, AssignmentType, Priority, Task


# Register your models here.
admin.site.register(ClassList)
admin.site.register(AssignmentType)
admin.site.register(Priority)
admin.site.register(Task)