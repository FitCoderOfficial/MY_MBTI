from django.contrib import admin
from .models import UserProfile, Test, Answer

admin.site.register(UserProfile)
admin.site.register(Test)
admin.site.register(Answer)