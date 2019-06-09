from rest_framework.viewsets import ModelViewSet
from doghouse.models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    filter_fields = ('nome', 'tipo_animal', 'cor_pelos', 'adotado')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        tipo_animal = self.request.query_params.get('tipo_animal', None)
        cor_pelos = self.request.query_params.get('cor_pelos', None)
        adotado = self.request.query_params.get('adotado', None)

        queryset = Animal.objects.all()

        if id:
            queryset = Animal.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if tipo_animal:
            queryset = queryset.filter(tipo_animal=tipo_animal)
        if adotado:
            queryset = queryset.filter(adotado=adotado.capitalize())
        if cor_pelos:
            queryset = queryset.filter(cor_pelos=cor_pelos)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(AnimalViewSet, self).partial_update(request, *args, **kwargs)
    
