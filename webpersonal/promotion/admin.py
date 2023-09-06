from django.contrib import admin
from . models import Promotion
# Register your models here.

class promotionAdmin(admin.ModelAdmin):
     readonly_fields=('created','updated')
admin.site.register(Promotion, promotionAdmin)