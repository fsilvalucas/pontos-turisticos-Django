from rest_framework.filters import SearchFilter
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
    search fields:
    # ^ : istartwith, Comeca com
    # = : iexact, Busca exata
    # @ : search, Mysql
    # $ : iregex, regex
    """
    #
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', '^endereco__linha1')
    # Pode ser usado ao inves do id, melhor manter o id, pois sabemos que ele eh primary key
    # lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        # Isso eh feito em lazy load, ou seja, a execucao real so acontece em return
        # refatoramos nosso queryset para que seja mais flexivel em relacao as queries
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        # A real execucao do queryset acontece aqui
        return queryset

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


