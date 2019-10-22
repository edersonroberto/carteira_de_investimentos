from django.urls import path

from .views import (
    transacao_detail_page, 
    carteira_list_view, 
    transacao_create_view,
    #transacao_retrieve_view,
    transacao_update_view,
    transacao_delete_view,
    transacao_list_view,
    carteira_delete_view,
    dividendos_list_view,
    dividendo_create_view,
    ticker_list_view,
    ticker_delete_view
)


urlpatterns = [
    path('transacao_new/', transacao_create_view),
    path('transacao_list/', transacao_list_view),
    path('transacao/<int:id>/edit/', transacao_update_view),
    path('transacao/<int:id>/delete/', transacao_delete_view),
    path('transacao/<str:ticker>/', transacao_detail_page),
    path('ticker_list/', ticker_list_view),
    path('ticker/<int:id>/delete/', ticker_delete_view),
    path('dividendo_new/', dividendo_create_view),
    path('dividendos_list/', dividendos_list_view),
   # path('transacao-retrieve/', transacao_create_view),

    path('', carteira_list_view),
]
