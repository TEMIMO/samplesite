from django.urls import path

from bboard.views import index, by_rubric
from .views import BbCreateView
urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
]