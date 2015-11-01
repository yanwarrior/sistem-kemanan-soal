from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages

from soal.models import Kelas
from soal.models import MataPelajaran
from soal.models import Guru
from soal.models import Soal
from soal.models import PasswordManager
from soal.extra.rc4 import InstanceRC4File


class AdminSiteTU(AdminSite):
    site_header = "Sistem Pengamanan Soal Ujian - SMA 90 Tangerang"

admin_site_tu = AdminSiteTU(name='adminsitetu')


class ModelAdminKelas(ModelAdmin):
    pass

class ModelAdminMataPelajaran(ModelAdmin):
    pass

class ModelAdminInlineGuru(TabularInline):
    model = Guru
    can_delete = False
    verbose_name_plural = 'Guru'

class UserAdminUserTU(UserAdmin):
    inlines = (ModelAdminInlineGuru,)

class UserAdminGroup(UserAdmin):
    pass

class ModelAdminSoal(ModelAdmin):
    list_display = [
        'list_display_nama_soal', 'list_display_tipe_file_soal',
        'list_display_ukuran_file_soal','tanggal', 'list_display_pemilik_soal',
        'list_display_status_dekripsi_soal',
    ]

    list_filter = ['tanggal', 'guru', 'status']
    
    view_on_site = False
    exclude = ('file_soal', 'guru',)
    actions = ['action_admin_dekripsi_soal']

    def action_admin_dekripsi_soal(self, request, queryset):
        print queryset.count()
        # cek apakah yang di ceklis ada soal yang sudah di dekrip
        if queryset.filter(status=True).count() == 0:
            # beri batasan brute dekripsi
            if queryset.filter(status=False).count() > 3:
                messages.warning(request, 'Jumlah batas dekripsi tidak boleh lebih dari 3.')
            else:
                for soal in queryset.filter(status=False):
                    InstanceRC4File.run(soal)
                    soal.status = True
                    soal.save()
        # jika soal yang di ceklis tidak ada soal yang sudah di dekrip
        else:
            messages.error(request, "Tidak bisa melakukan dekripsi, karena terdapat soal yang sudah di dekripsi")
    action_admin_dekripsi_soal.short_description = "Dekrip Soal & Unduh"

class ModelAdminPasswordManager(ModelAdmin):
    list_display = [
        'list_display_username_guru', 'password', 
        'list_display_soal_guru', 'list_display_soal_guru_dekripsi',
    ]

# admin site khusus TU
admin_site_tu.register(Kelas, ModelAdminKelas)
admin_site_tu.register(MataPelajaran, ModelAdminMataPelajaran)
admin_site_tu.register(Soal, ModelAdminSoal)
admin_site_tu.register(PasswordManager, ModelAdminPasswordManager)
admin_site_tu.register(User, UserAdminUserTU)
admin_site_tu.register(Group)

