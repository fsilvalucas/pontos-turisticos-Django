from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSets(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # Filter based in django_filters extensions
    filter_fields = ('nome', 'descricao')
