from django.contrib import admin
from .models import *

# Register your models here.
#username : admin
#password : 12345


admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Patient)
admin.site.register(Lab)
