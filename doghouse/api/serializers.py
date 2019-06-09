from rest_framework.serializers import ModelSerializer
from doghouse.models import Animal


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            'id', 'nome', 'descricao', 'tipo_animal', 'raca', 
            'cor_pelos', 'cor_olhos', 'tipo_pelagem', 'data_nascimento', 
            'data_resgate', 'adotado', 'foto'
            )


