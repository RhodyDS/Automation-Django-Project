from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_Dashboard, name="dashboard"),
    path("automacao/", views.automacao_view, name="automacao"),
    path("notificação/", views.automation_function, name="notifica"),
]
