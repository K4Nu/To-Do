from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.task_form, name="form"),  # Removed the leading slash
]
