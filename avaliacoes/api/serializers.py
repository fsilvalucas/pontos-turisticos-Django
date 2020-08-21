from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
