from django.urls import path, include

from .views import PaginaResumoMensal, Pendencias, PaginaInicial, PaginaSobre, PaginaCartao, PaginaResumoAnual


urlpatterns = [

    path('', PaginaInicial.as_view(), name='index'),
    path('pendencias/<str:mes>', Pendencias.as_view(), name='pendencias'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
    path('cartao/<int:id>/<str:mes>', PaginaCartao.as_view(), name='cartao'),
    path('resumo-mensal/<int:ano>', PaginaResumoMensal.as_view(), name='resumo-mensal'),
    path('resumo-anual/<int:ano>', PaginaResumoAnual.as_view(), name='resumo-anual'),
    path('', include('cadastros.urls')),
]