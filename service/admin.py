from django.contrib import admin

from .models import Service, Package


class ServiceAdmin(admin.ModelAdmin):
    ...


class PackageAdmin(admin.ModelAdmin):
    ...


admin.site.register(Service, ServiceAdmin)
admin.site.register(Package, PackageAdmin)
