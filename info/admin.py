from django.contrib import admin

from .models import ContactUs, MainInfo, TeamMember


class MainInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('whatsapp_link', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class ContactUsAdmin(admin.ModelAdmin):
    ...


class TeamMemberAdmin(admin.ModelAdmin):
    ...


admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
