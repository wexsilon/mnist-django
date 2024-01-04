from django.urls import path
from .views import show_form, get_result

urlpatterns = [
    path('', show_form),
    path('result/', get_result, name='get_result')
]
