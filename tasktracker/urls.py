from django.urls import path, include
from . import views

urlpatterns = [
    # Authentication & Authorization
    path('newregistration', views.newregistration, name='newregistration'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),

    # User Specific Access
    path('addorupdatetask', views.addorupdatetask, name='addtask'),
    path('addorupdatetask/<int:id>/', views.addorupdatetask, name='updatetask'),
    path('timetask/<int:id>/', views.timetask, name='timetask'),
    path('deletetask/<int:id>/', views.deletetask, name='deletetask'),
    path('listalltasks/', views.listalltasks, name='listalltasks'),

    # Admin Specific Access
    path('addorupdateproject', views.addorupdateproject, name='addproject'),
    path('addorupdateproject/<int:id>/', views.addorupdateproject, name='updateproject'),
    path('deleteproject/<int:id>/', views.deleteproject, name='deleteproject'),
    path('listallprojects/', views.listallprojects, name='listallprojects')
]
