from django.urls import path
from Accounting import views


urlpatterns=[
    path('record_list/',views.record_list),
    path('record_details/<int:record_id>/',views.record_details)
] 