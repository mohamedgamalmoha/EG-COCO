from django.contrib import admin

from .models import PackageOrder, CustomOrder


class PackageOrderAdmin(admin.ModelAdmin):
    ...


class CustomOrderAdmin(admin.ModelAdmin):
    ...


admin.site.register(CustomOrder, CustomOrderAdmin)
admin.site.register(PackageOrder, PackageOrderAdmin)
