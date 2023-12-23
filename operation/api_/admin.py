from django.contrib import admin
from .models import Users,file_datas,operation

# Register your models here.
admin.site.register(Users)
admin.site.register(file_datas)
admin.site.register(operation)