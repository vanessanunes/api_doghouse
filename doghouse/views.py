from rest_framework import generics
from .api.serializers import AnimalSerializer
from .models import Animal

class AnimaisList(generics.ListCreateAPIView):
    """
        Listagem e criação
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetalhes(generics.RetrieveUpdateDestroyAPIView):
    """
        Atualizar, excluir e atualizar 
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

