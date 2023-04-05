from django.urls import path
from . import views

# accounts/
# accounts/1/details

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('<int:user_id>', views.detail, name='accounts_detail')
]
