from django.urls import path
from .views import dynamic_template_view, home

urlpatterns = [
    path('', home, name='home'),
    path('<str:template_name>/', dynamic_template_view, name='dynamic_template'),
]
