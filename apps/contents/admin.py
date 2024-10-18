from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.contents.models import (
    Car, Contact, CarImage
)

from django.utils.safestring import mark_safe
from django.urls import reverse


class CarResource(resources.ModelResource):
    class Meta:
        model = Car
        fields = [
            'id', 'status', 'brand', 'model', 'city', 'color',
            'year', 'drive_type', 'fuel_type', 'volume',
            'volume_description', 'description', 'interior_description',
            'why_this_car', 'created_at', 'updated_at'
        ]


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    resource_class = CarResource
    list_display = (
        'get_name', 'status', 'year', 'color',
        'volume', 'volume_description', 'city'
    )
    list_editable = ('status',)
    list_filter = ('city', 'status', 'fuel_type', 'year')
    search_fields = ('brand', 'model', 'license_plate', 'color')
    ordering = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('brand', 'model', 'year', 'color', 'city', 'status', 'license_plate')
        }),
        ('Технические данные', {
            'fields': ('drive_type', 'fuel_type', 'volume', 'volume_description')
        }),
        ('Описание', {
            'fields': ('description', 'interior_description', 'why_this_car')
        }),
        ('Цены на аренду', {
            'fields': ('price_6_hours', 'price_12_hours', 'price_24_hours')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    get_name.short_description = 'Название автомобиля'


class CarImageResource(resources.ModelResource):
    class Meta:
        model = CarImage
        fields = ['id', 'image']


# Custom admin for CarImage model
@admin.register(CarImage)
class CarImageAdmin(ImportExportModelAdmin):
    resource_class = CarImageResource
    list_display = ('view_image', 'car_name', 'id', 'created_at',
                    'updated_at')
    search_fields = ('image',)
    ordering = ('-id',)

    fieldsets = (
        (None, {
            'fields': ('image', 'car')
        }),
    )

    def view_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" />')
        else:
            return 'No image'

    # Метод для отображения ссылки на редактирование машины
    def car_name(self, obj: Car):
        return obj.get_name()

    car_name.short_description = 'Car'


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = [
            'id', 'full_name', 'phone_number', 'date_start',
            'date_end', 'city', 'auto', 'is_read', 'created_at', 'updated_at'
        ]


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ('full_name', 'phone_number', 'date_start',
                    'date_end', 'city', 'is_read', 'created_at')
    list_filter = ('city', 'is_read')
    search_fields = ('full_name', 'phone_number')
    ordering = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('full_name', 'phone_number', 'date_start', 'date_end', 'city', 'auto', 'is_read')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )