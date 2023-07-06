from django.urls import path
from . import views

# Handle index urls
urlpatterns = [
    path('', views.index, name='home')
]
