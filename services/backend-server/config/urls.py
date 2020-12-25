from .views import tick
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Museum Wiki API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tick", tick, name="tick"),
    path("swagger-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("wiki.urls")),
]
