from django.contrib import admin

from .models import ContactUs, MainInfo, TeamMember, FAQs, PreviousProject, SubscribedEmails, Company


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


class FAQsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active', 'created', 'updated')


class PreviousProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active', 'created', 'updated')


class SubscribedEmailsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'updated')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'updated')


admin.site.register(FAQs, FAQsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(PreviousProject, PreviousProjectAdmin)
admin.site.register(SubscribedEmails, SubscribedEmailsAdmin)
