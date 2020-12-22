from django.urls import path

from .views import WikiList, WikiDetail

urlpatterns = [
    path('api/v1/wiki/', WikiList.as_view()),
    path('api/v1/wiki/<int:pk>/', WikiDetail.as_view())

]
