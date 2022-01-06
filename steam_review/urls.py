from django.urls import path
from .views import HomePageView, HelloView, ResultView


urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
    path('result/', ResultView.as_view(), name='result'),
]