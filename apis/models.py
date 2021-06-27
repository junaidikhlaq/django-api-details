from django.db import models
from django.db.models import Sum, F


class Contact(models.Model):
    CONTACT_TYPES = [
        ('PRIVATE', 'Private'),
        ('COMPANY', 'Company'),
    ]
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    type = models.CharField(max_length=20, choices=CONTACT_TYPES, default='PRIVATE')
    salutation = models.CharField(max_length=256)

    def __str__(self):
        return self.email

    @property
    def addresses(self):
        return self.address_set.all()

    @property
    def address_count(self):
        return self.address_set.all().count()


class Country(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    value = models.CharField(max_length=256)

    def __str__(self):
        return "{} ({})".format(self.key, self.value)


class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.street, self.city, self.country.key)


class Invoice(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    invoice_date = models.DateField()
    due_date = models.DateField()
    condition = models.CharField(max_length=256)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    @property
    def total_amount(self):
        return self.invoiceposition_set.all().aggregate(total=Sum(
            F('quantity') *
            F('amount'),
            output_field=models.FloatField()
        )).get('total', 0)
        # return self.invoiceposition_set.all().count()

    @property
    def contact_name(self):
        return self.address.contact.name

    @property
    def positions(self):
        return self.invoiceposition_set.all()


class InvoicePosition(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(decimal_places=1, max_digits=10)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    @property
    def total(self):
        return self.quantity * self.amount
