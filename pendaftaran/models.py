from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_lenght=100)
    Jenis_kelamin = models.CharField(max_lenght=10)
    asal_sekolah = models.CharField(max_lenght=100)

    def --str--(self):
        return self.nama

class OrangTua(models.Model):
    nama = models.CharField(max_lenght=100)   
    pekerjaan = models.CharField(max_lenght=100)

    def --str--(self): 
        return self.nama
        
