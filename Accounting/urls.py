from django.urls import path
from Accounting import views

app_name ='accounting'
urlpatterns=[
    path('record_list/',views.record_list,name="record_list"),
    path('record_details/<int:record_id>/',views.record_details,name='record_details')
] 