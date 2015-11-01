from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from soal.models import Kelas
from soal.models import MataPelajaran
from soal.models import Guru
from soal.models import Soal
from soal.models import PasswordManager


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
    pass

class ModelAdminPasswordManager(ModelAdmin):
    list_display = [
        'list_display_username_guru', 'password', 
        'list_display_soal_guru', 'list_display_soal_guru_dekripsi'
    ]

# admin site khusus TU
admin_site_tu.register(Kelas, ModelAdminKelas)
admin_site_tu.register(MataPelajaran, ModelAdminMataPelajaran)
admin_site_tu.register(Soal, ModelAdminSoal)
admin_site_tu.register(PasswordManager, ModelAdminPasswordManager)
admin_site_tu.register(User, UserAdminUserTU)
admin_site_tu.register(Group)

