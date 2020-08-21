from rest_framework.viewsets import ModelViewSet
from localizacao.models import Endereco
from localizacao.api.serializers import EnderecoSerializer


class EnderecoViewSets(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
