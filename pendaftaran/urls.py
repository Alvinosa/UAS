from django.urls import path
from . import views

urlpatterns = [
    path('', views.pendaftaran_siswa, name='penfataran_siswa'),
    path('sukses/', views.sukses_pendaftaran, name='sukses_pendaftaran'),
]