from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    # define your fields here

    def save_model(self, request, obj, form, change):
        obj.gallery_id = form.cleaned_data['gallery'].id
        obj.save()

admin.site.register(Image, ImageAdmin)