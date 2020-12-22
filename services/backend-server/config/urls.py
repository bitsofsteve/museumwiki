from django.contrib import admin
from django.urls import path, include

from .views import tick

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tick", tick, name="tick"),
    path("", include("wiki.urls")),
]
