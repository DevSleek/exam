from django.contrib import admin
from .models import Region, District, School, Student, Test


admin.site.register([Region, District, School, Student, Test])
