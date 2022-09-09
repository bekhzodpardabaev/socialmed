from django.contrib import admin
from .models import News, Organization, MedicalCategory, Services, Categories, Apply
# Register your models here.
admin.site.register(Apply)
admin.site.register(News)
admin.site.register(Organization)
admin.site.register(MedicalCategory)
admin.site.register(Services)
admin.site.register(Categories)