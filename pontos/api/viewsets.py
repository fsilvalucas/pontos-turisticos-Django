from rest_framework.viewsets import ModelViewSet
# App
from pontos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# Model viewset ja implementa um CRUD completo, `create()`, `retrieve()`, `update()`,
#     `partial_update()`, `destroy()` e `list()`


class PontoTuristicoViewSet(ModelViewSet):
    """
    EndPoint para a listagem de todos os pontos turisticos com o CRUD completo
    herdade de ModelViewSet
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # estamos sobreescrevendo o meteodo, porem chamamos o metodo original da classe mae
    # o comportamento continua o mesmo de antes. Mas estamos vendo a referencia
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self,  request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self,  request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)


