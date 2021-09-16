from django.urls import path

from .views import *

urlpatterns = (
    path('', home, name='home'),
    path('add/', AddressChoiceCreate.as_view(), name='add'),
    path('<int:address_id>/vote/', vote, name='vote')
)
