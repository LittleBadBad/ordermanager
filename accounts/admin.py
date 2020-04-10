from django.contrib import admin
from accounts.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(User)