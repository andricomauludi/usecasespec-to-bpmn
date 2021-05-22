from django.urls import path
from . import views
from app import views as blogViews


urlpatterns = [
    path('', views.index, name="index"),
    path('project_list_form/', views.createproject),
    path('update_project/<str:pk>/',views.updateproject),
]