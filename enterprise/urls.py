from django.urls import path

from enterprise.views import ResultCreateAPIView

urlpatterns = [
    path('request/', ResultCreateAPIView.as_view()),
]