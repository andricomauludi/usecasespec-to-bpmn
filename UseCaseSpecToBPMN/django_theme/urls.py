from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('project_list/', include('project_list.urls')),
    path('bpmn_list/', include('bpmn_list.urls')),
]
