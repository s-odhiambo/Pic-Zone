from django.contrib import admin
from .models import  Image,Location,Category

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display =["title", "post_date"]

    class Meta:
        model = Image
        
admin.site.register(Image,ImageAdmin)
admin.site.register(Location )
admin.site.register(Category)