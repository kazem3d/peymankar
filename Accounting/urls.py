from django.urls import path
from Accounting import views

urlpatterns=[
    path('record_list/',views.record_list)
]