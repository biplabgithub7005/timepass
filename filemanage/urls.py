
from django.urls import path
from . import views as file_views



urlpatterns = [
    path('', file_views.show_pdf, name='show-pdf'),
]