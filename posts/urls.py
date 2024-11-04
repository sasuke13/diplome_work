from django.urls import path
from .views import dynamic_template_view, home, english_dynamic_template_view, en_home

urlpatterns = [
    path('', home, name='home'),
    path('en/', en_home, name='en_home'),
    path('en/<str:template_name>/', english_dynamic_template_view, name='english_dynamic_template_view'),
    path('<str:template_name>/', dynamic_template_view, name='dynamic_template'),
]
