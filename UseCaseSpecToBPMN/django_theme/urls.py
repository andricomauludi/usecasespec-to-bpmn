from django.contrib import admin
from django.urls import path, include
from . import views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('project_list/', include('project_list.urls')),
    path('bpmn_list/', include('bpmn_list.urls')),
]
