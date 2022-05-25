from django.contrib import admin

# Register your models here.
from .models import info, user

admin.site.register(info)
admin.site.register(user)