from django.urls import path
from . import views

app_name = 'financials'

urlpatterns = [

    path('', views.index, name='index'),
    path('stock_info/', views.stock_info, name='stock_info'),
    path('stock_info/<str:symbol>/', views.stock_info, name='stock_info_symbol'),

]

