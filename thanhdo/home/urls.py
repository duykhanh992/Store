from django.urls import path

from . import  views


urlpatterns = [
    path('',views.Customerview, name='homepage'),
    path('form',views.formview),
    path('employeeview',views.employeeview,name='employeeview')
]