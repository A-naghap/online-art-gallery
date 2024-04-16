#from django.contrib import admin
#from .models import CustomUser  # Import your model

#admin.site.register(CustomUser)  # Register your model with the admin interface
#from django.contrib import admin
#from . models import Staff
# Register your models here.
#admin.site.register(Staff)
#from django.contrib import admin
#from .models import CustomUser  # Import your model

#admin.site.register(CustomUser)  # Register your model with the admin interface


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'user_type', 'first_name', 'last_name', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )

#admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib.auth import get_user_model

User = get_user_model()

class SuperuserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return User.objects.filter(is_superuser=False)
    list_display=('email','username')

# Register the custom admin class
admin.site.register(User, SuperuserAdmin)
admin.site.register(Product),
admin.site.register(AuctionProduct),

admin.site.register(Competition),
admin.site.register(Bid)


