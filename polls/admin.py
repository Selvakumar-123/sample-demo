from django.contrib import admin
from django.contrib import admin

from .models import Question
from .models import Employee_Details
from .models import Employee

# Register your models here.
admin.site.register(Question)
admin.site.register(Employee_Details)
admin.site.register(Employee)




