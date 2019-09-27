from django.urls import path

from .views import (
    transacao_detail_page, 
    carteira_list_view, 
    transacao_create_view,
    transacao_retrieve_view,
    transacao_update_view,
    transacao_delete_view
)


urlpatterns = [
    path('transacao-new/', transacao_create_view),
   # path('transacao-retrieve/', transacao_create_view),
    path('transacao/<str:ticker>/edit/', transacao_update_view),
    path('transacao/<str:ticker>/delete/', transacao_delete_view),
    path('transacao/<str:ticker>/', transacao_detail_page),
    path('', carteira_list_view),
]
