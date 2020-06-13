from django.contrib import admin
from .models import Headline, Category
# Register your models here.

admin.site.register(Category)

@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title','url')
    list_filter  = ['date',]
