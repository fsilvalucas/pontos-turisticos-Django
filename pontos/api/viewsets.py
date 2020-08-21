from rest_framework.viewsets import ModelViewSet

# App
from pontos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# Model viewset ja implementa um CRUD completo, `create()`, `retrieve()`, `update()`,
#     `partial_update()`, `destroy()` e `list()`


class PontosTuristicosViewSet(ModelViewSet):
    """
    EndPoint para a listagem de todos os pontos turisticos com o CRUD completo
    herdade de ModelViewSet
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
