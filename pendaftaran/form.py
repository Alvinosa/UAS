from django import forms
from .models import Siswa, OrangTua

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ['nama', 'Jenis_kelamin', 'asal_sekolah']

 class OrangTuaForm(forms.ModelForm):
    class Meta:
        model = OrangTua
        fields = ['nama', 'pekerjaan']