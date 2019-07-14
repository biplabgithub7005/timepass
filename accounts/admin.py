from django.contrib import admin

# Register your models here.
from .models import Signup,UserProfile
# Register your models here.
admin.site.register(Signup)
admin.site.register(UserProfile)