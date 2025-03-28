from django.contrib import admin
from .models import Package, About,  Review

# Register your models here.
admin.site.register(Package)
admin.site.register(About)
admin.site.register(Review)