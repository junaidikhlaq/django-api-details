from django.contrib import admin
from .models import Invoice, InvoicePosition, Address, Contact, Country


class AddressAdminInline(admin.TabularInline):
    model = Address
    extra = 0


class InvoicePositionInline(admin.TabularInline):
    model = InvoicePosition
    extra = 0


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_filter = ('type',)
    list_display = ('name', 'email', 'type', 'address_count',)
    search_fields = ('name', 'email',)
    inlines = [AddressAdminInline, ]


class CountryAdmin(admin.ModelAdmin):
    model = Country

    search_fields = ('key', 'value',)
    list_display = ('key', 'value',)


class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice

    list_display = ('contact_name', 'due_date', 'total_amount',)
    search_fields = ('address__contact__name', 'title',)
    inlines = [InvoicePositionInline, ]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoicePosition)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)
