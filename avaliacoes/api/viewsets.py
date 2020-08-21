from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvalizacaoSerializer


class ComentarioViewSets(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalizacaoSerializer
