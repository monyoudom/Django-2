from django.contrib import admin
from django.urls import path
from ReservationTool import views

app_name = "reservationtool"

urlpatterns = [
    path("", views.home, name='home'),
    path("add_device/", views.add_device, name='add_device'),
    path("view_device/", views.view_device, name='view_device'),
    path("add_setup/", views.AddSetupView.as_view(), name='add_setup'),
    path("view_setup/", views.view_setup, name='view_setup'),
    path("export/", views.export, name='export'),
    path("export/set-up", views.export_set_up, name='export'),
]
