from django.contrib import admin
from .models import Package, About,  Review, Appointment

# Register your models here.
admin.site.register(Package)
admin.site.register(About)
admin.site.register(Review)
admin.site.register(Appointment)