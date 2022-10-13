from django.contrib import admin
from .models import PostModel,Commnent
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')

    
admin.site.register(PostModel,PostModelAdmin)
admin.site.register(Commnent)
