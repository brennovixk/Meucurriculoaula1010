from django.urls import path
from . import views


app_name = 'curriculo'

urlpatterns = [

    path('brenno/', views.curriculo_brenno, name='brenno'),


    path('spiff/', views.curriculo_spiff, name='spiff'),
]