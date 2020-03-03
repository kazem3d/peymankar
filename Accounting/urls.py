from django.urls import path
from Accounting import views

app_name ='accounting'
urlpatterns=[
  
    path('record_list/',views.record_list,name="record_list"),
    path('record_details/<int:record_id>/',views.record_details,name='record_details'),
    path('record_register/',views.record_register,name='record_register'),
    path('project_register/',views.project_register,name='project_register'),
    path('projects_list/',views.projects_list,name='projects_list'),
    path('about/',views.about_us,name='about_us'),
    path('project_details/<int:project_id>',views.project_details,name='project_details'),
    path('project_edit/<int:project_edit_id>',views.project_edit,name='project_edit'),
    path('record_edit/<int:record_edit_id>/',views.record_edit,name='record_edit')


] 