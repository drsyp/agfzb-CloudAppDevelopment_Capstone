from django.contrib import admin
from .models import CarModel, CarMake

# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    fields = ['id','name', 'year', 'car_make', 'dealer_id', 'type']

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['id','name', 'description']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
