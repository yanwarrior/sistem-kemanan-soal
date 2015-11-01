from django.db import models
from django.contrib.auth.models import User


class Kelas(models.Model):
    kelas = models.CharField(max_length=4, unique=True)
    
    def __str__(self):
        return self.kelas

    class Meta:
        verbose_name_plural = "Data Kelas"
        

class MataPelajaran(models.Model):
    mata_pelajaran = models.CharField(max_length=20)

    def __str__(self):
        return self.mata_pelajaran

    class Meta:
        verbose_name_plural = "Data Mata Pelajaran"


class Guru(models.Model):
    username = models.OneToOneField(User)
    mata_pelajaran = models.ForeignKey(MataPelajaran)
    mengajar = models.ManyToManyField(Kelas)

    def __str__(self):
        return self.username.username

class PasswordManager(models.Model):
    guru = models.OneToOneField(Guru)
    password = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.guru.username.username

    class Meta:
        verbose_name_plural = "Manajemen Password"

class Soal(models.Model):
    file_soal = models.FileField(upload_to='documents/%Y/%m/%d')
    tanggal = models.DateTimeField(auto_now_add=True, blank=True)
    guru = models.ForeignKey(Guru)
    status = models.BooleanField(blank=True, default=False)

    def filename(self):
        return self.file_soal.name.split("/")[-1]

    def type_file(self):
        return self.file_soal.name.split(".")[-1]
    
    def __str__(self):
        return self.file_soal.name

    # TODO: add method checklist, for auto checklist status to True

    class Meta:
        verbose_name_plural = "Data Soal"




