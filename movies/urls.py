from django.urls import path
from . import views

# movies/
# movies/1/details
# movies/

# /movies/1
# /old_system/movies/1

urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
