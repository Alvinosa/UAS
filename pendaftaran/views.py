from django.shortcuts import render, redirect
from .forms import SiswaForm, OrangTuaForm

def pendaftaran_siswa(request):
    if request.method == 'POST':
        siswa_form = SiswaForm(request.POST)
        orang_tua_form = OrangTuaForm(request.POST)
        if siswa_form.is_valid() and orang_tua_form.is_valid():
            siswa = siswa_form.save()
            orang_tua = orang_tua_form.save()
            return redirect('sukses_pendaftaran')
    
    else:
        siswa_form = SiswaForm()
        orang_tua_form = OrangTuaForm()
    return render(request, 'pendaftaran/pendaftaran.html', {'siswa_form': siswa_form, 'orang_tua_form': orang_tua_form})

def sukses_pendaftaran(request):
    return render(request, 'pendaftaran/sukses_pendaftaran.html')
