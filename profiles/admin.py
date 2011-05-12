from django.contrib import admin
from blogserver.profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
