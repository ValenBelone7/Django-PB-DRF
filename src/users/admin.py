from django.contrib import admin

from .models import CheckIn, Heredero, Herencia, User

admin.site.register(User)
admin.site.register(Heredero)
admin.site.register(CheckIn)
admin.site.register(Herencia)
