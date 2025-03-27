from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('detalhe/<int:id>/', views.detalhe_ocorrencia, name='detalhe_ocorrencia'),
]