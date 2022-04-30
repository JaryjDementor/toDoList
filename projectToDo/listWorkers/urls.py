from django.urls import path

from .views import list_workers

urlpatterns = [
    path("list-workers", list_workers, name="list_workers"),
]