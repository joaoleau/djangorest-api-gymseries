from django.contrib import admin
from .models import UserConfirmation, User

admin.site.register(User)
admin.site.register(UserConfirmation)
