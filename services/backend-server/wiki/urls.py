from django.urls import path

from .views import WikiList, WikiDetail

urlpatterns = [
    path('<int:pk>/', WikiDetail.as_view()),
    path('', WikiList.as_view())
]