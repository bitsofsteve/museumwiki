from django.urls import path

from .views import WikiList

urlpatterns = [
    # path('<int:pk>/', WikiDetail.as_view()),
    path('api/v1/wiki/', WikiList.as_view())
]