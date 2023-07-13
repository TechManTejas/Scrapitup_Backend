from django.contrib import admin
from scrapitup_backend.utilities import export_to_excel
from customer.models import Customer
from vendor.models import ScrapPartner
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomerInline(admin.TabularInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customer'
    fk_name = 'user'


class ScrapPartnerInline(admin.TabularInline):
    model = ScrapPartner
    can_delete = False
    verbose_name_plural = 'scrap_partner'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    actions = [export_to_excel]

    def get_inline_instances(self, request, obj=None):
        if obj is not None and hasattr(obj, 'customer'):
            return [CustomerInline(self.model, self.admin_site)]
        elif obj is not None and hasattr(obj, 'scrap_partner'):
            return [ScrapPartnerInline(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
