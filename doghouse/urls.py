from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AnimaisList, AnimalDetalhes

urlpatterns = [
    path('', AnimaisList.as_view()),
    path('<int:pk>', AnimalDetalhes.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)