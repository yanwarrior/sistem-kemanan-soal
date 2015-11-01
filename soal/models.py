from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.conf import settings


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

    def list_display_username_guru(self):
        return self.guru.username.username
    list_display_username_guru.short_description = "Guru"

    def list_display_soal_guru(self):
        return self.guru.soal_set.count()
    list_display_soal_guru.short_description = "Banyak Soal"

    def list_display_soal_guru_dekripsi(self):
        return self.guru.soal_set.filter(status=True).count()
    list_display_soal_guru_dekripsi.short_description = "Soal Dekripsi"
        
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

    def list_display_nama_soal(self):
        return self.file_soal.name.split("/")[-1]
    list_display_nama_soal.short_description = "Soal"

    def list_display_tipe_file_soal(self):
        return self.file_soal.name.split(".")[-1]
    list_display_tipe_file_soal.short_description = "Tipe File"

    def list_display_pemilik_soal(self):
        return self.guru.username.username
    list_display_pemilik_soal.short_description = "Guru"

    def list_display_status_dekripsi_soal(self):
        return self.status
    list_display_status_dekripsi_soal.short_description = "Status Dekripsi ?"
    list_display_status_dekripsi_soal.boolean = True

    def list_display_ukuran_file_soal(self):
        return "{:.2f} Kb".format(float(self.file_soal.size) / 1024)
    list_display_ukuran_file_soal.short_description = "Ukuran"

    def list_display_download_soal(self):
        if self.status:
            html = """
                <a href="{}" target='_blank'>Unduh Soal</a>
            """.format(settings.MEDIA_URL + self.file_soal.name)
        else:
            html = """
            <a href="{}" target='_blank' onclick='alert("file ini belum di dekripsi !")'>Unduh Soal</a>
            """.format(settings.MEDIA_URL + self.file_soal.name)
        return format_html(html)
    list_display_download_soal.short_description = "Unduh"
    list_display_download_soal.allow_tag = True
    
    def __str__(self):
        return self.file_soal.name

    # TODO: add method checklist, for auto checklist status to True

    class Meta:
        verbose_name_plural = "Data Soal"




