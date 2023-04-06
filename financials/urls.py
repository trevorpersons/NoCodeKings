from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='financials_index'),

    path('stock_info/', views.stock_info, name='stock_info'),
    
    path('stock_info/<str:symbol>/', views.stock_info, name='stock_info_symbol'),

]

