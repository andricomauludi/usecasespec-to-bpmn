from django.urls import path
from . import views
from app import views as blogViews
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('project_list_form/', views.createproject),
    path('update_project/<str:pk>/',views.updateproject),
    path('scenario_list/<slug:no>', views.indexscenario, name="index"),
    path('scenario_list/scenario_list_form/', views.createscenario),
    path('scenario_list/scenario_update/<str:pk>', views.updatescenario),
    path('scenario_list/scenario_delete/<str:pk>', views.deletescenario),
    path('Generate/', views.Generate),
]
