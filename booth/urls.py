from django.urls import path
from .views import *

app_name = 'booth'

urlpatterns = [
    path('', BoothListView.as_view()),
    path('<int:pk>/', BoothDetailView.as_view()),
]