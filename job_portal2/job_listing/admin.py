from django.contrib import admin
from .models import JobDB

@admin.register(JobDB)
class JobDBAdmin(admin.ModelAdmin):
    list_display=['id','title','location','salary','experience']
    