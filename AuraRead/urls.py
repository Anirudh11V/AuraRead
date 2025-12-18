from django.urls import path
from . import views

app_name = 'AuraRead'

urlpatterns = [
    path('', views.Upload, name= 'upload_file'),
    path('select/<int:pdf_id>/', views.select_range, name= 'select_range'),
    path('listen/<int:pdf_id>/', views.listen_audio, name= 'listen_audio'),
]