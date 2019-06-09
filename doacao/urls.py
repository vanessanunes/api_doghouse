from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from doghouse.api.viewsets import AnimalViewSet

routers = routers.DefaultRouter()
routers.register(r'animal', AnimalViewSet, base_name='Animal')

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
