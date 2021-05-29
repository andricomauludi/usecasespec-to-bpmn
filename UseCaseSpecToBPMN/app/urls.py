from django.urls import path
from . import views
from app import views as blogViews


urlpatterns = [
    path('', views.index, name="home"),
]
