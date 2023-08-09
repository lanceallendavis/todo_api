from django.urls import path
from todo import views

from . import views

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:pk>/", views.detail, name="detail"),
    path("status/", views.status, name="status"),
    path("reorder/", views.reorder, name="reorder"),
]