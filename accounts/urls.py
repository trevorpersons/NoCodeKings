from django.urls import path
from . import views

# accounts/
# accounts/1/details
app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.detail, name='detail')
]
