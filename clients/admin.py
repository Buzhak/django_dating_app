from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'get_img')
    readonly_fields = ('avatar',)
    fields = ('first_name', 'last_name', 'gender', 'email', 'avatar')


    def get_img(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="80px">')
        return "нет картинки"
    get_img.short_description = "Фото"

admin.site.register(Client, ClientAdmin)