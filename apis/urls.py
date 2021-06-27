from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apis import views

router = DefaultRouter()
router.register('contacts', viewset=views.ContactViewSet)
router.register('addresses', viewset=views.AddressViewSet)
router.register('invoices', viewset=views.InvoiceViewSet)
router.register('invoice_positions', viewset=views.InvoicePositionViewSet)

urlpatterns = [
                  path('countries/', views.CountryListView.as_view()),
                  path('get_token/', obtain_auth_token, name='api_token_auth'),
              ] + router.urls
