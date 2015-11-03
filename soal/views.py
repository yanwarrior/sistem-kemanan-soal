from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import SuspiciousFileOperation
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

from soal.models import Soal
from soal.models import Guru
from soal.models import PasswordManager
from soal.forms import FormSoal
from soal.extra.rc4 import InstanceRC4File



class SoalListView(ListView):
    """
    Show lists of soal after upload 
    from all status.
    """
    model = Soal
    template_name = "soal/soal_list.html"
    paginate_by = 10

    q = ""
    
    def get_context_data(self, **kwargs):
        """                                                        
        overriding method on ListView class.
        this method to use custom list data
        from model Soal to show in template.
        """
        context = super(SoalListView, self).get_context_data(**kwargs)
        q = ""
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            list_soal = Soal.objects.filter(guru__username=self.request.user, file_soal__icontains=q)
        else:
            list_soal = Soal.objects.filter(guru__username=self.request.user)
            
        paginator = Paginator(list_soal, self.paginate_by)
        page = self.request.GET.get('page')
        
        try:
            soal = paginator.page(page)
        except PageNotAnInteger:
            soal = paginator.page(1)
        except EmptyPage:
            soal = paginator.page(paginator.num_pages)
            
        context['soal_list'] = soal
        context['guru'] = self.request.user
        context['q'] = q
        return context

    
    def dispatch(self, request, *args, **kwargs):
        """
        jika staff login ke halaman guru,
        maka staff akan langsung di bawa ke
        halaman admin site khusus TU.
        """

        # cek apakah yang masuk adalah staff atau TU ?
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        # cek apakah yang masuk ke sistem ini adalah superadmin
        # jika yang login adalah super user
        # maka sistem juga akan meredirect
        # super user ke halaman admin.
        if(request.user.is_superuser):
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        return super(SoalListView, self).dispatch(request, *args, **kwargs)


class SoalDeleteView(DeleteView):
    model = Soal
    success_url = reverse_lazy('soal:soal-view')
    template_name = 'soal/soal_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(SoalDeleteView, self).get_context_data(**kwargs)
        context['auth_member'] = self.request.user.username
        return context

    def delete(self, request, *args, **kwargs):
        print("hahaha",self.get_object(), type(self.get_object()))
        soal = self.get_object()
        
        if soal.guru.username.username != request.user.username:
            raise SuspiciousFileOperation("Sory, Operasi ini dilarang !")
        else:
            return super(SoalDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        soal = self.get_object()
        if soal.guru.username.username != request.user.username:
            raise Http404("Tidak ada soal yang dihapus")
        else:
            return super(SoalDeleteView, self).get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        """
        jika staff login ke halaman guru,
        maka staff akan langsung di bawa ke
        halaman admin site khusus TU.
        """

        # cek apakah yang masuk adalah staff atau TU ?
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        # cek apakah yang masuk ke sistem ini adalah superadmin
        # jika yang login adalah super user
        # maka sistem juga akan meredirect
        # super user ke halaman admin.
        if(request.user.is_superuser):
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        return super(SoalDeleteView, self).dispatch(request, *args, **kwargs)
    
class SoalCreateView(CreateView):
    form_class = FormSoal
    #fields = ['file_soal',]
    success_url = reverse_lazy('soal:soal-view')
    template_name = "soal/soal_form.html"
                
    def form_valid(self, form):
        form.instance.tanggal = timezone.now()
        user = self.request.user
        # TODO : Menambahkan algoritma enkripsi RC4 (ok)
        #print(list(form.instance.file_soal.read()))
        #print(settings.MEDIA_ROOT)
        #print(form.instance.file_soal.name)
        form.instance.guru = Guru.objects.get(username=user)
        return super(SoalCreateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        jika staff login ke halaman guru,
        maka staff akan langsung di bawa ke
        halaman admin site khusus TU.
        """

        # cek apakah yang masuk adalah staff atau TU ?
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        # cek apakah yang masuk ke sistem ini adalah superadmin
        # jika yang login adalah super user
        # maka sistem juga akan meredirect
        # super user ke halaman admin.
        if(request.user.is_superuser):
            return HttpResponseRedirect(reverse('adminsitetu:index'))

        return super(SoalCreateView, self).dispatch(request, *args, **kwargs)
    


def signal_to_encryption(sender, instance, created, **kwargs):
    """
    Django signals untuk mengenkripsi file setelah
    terjadinya penyimpana soal.
    """

    # jika created True itu artinya insert data ke database
    # jika created False itu artinya update data ke database
    if created:
        data_file = instance.file_soal.read()
        print("signal accessing")
        password = instance.guru.passwordmanager.password
        print(password)
        nama_file = instance.file_soal.path
        print(nama_file)
        InstanceRC4File.run(instance)

def signal_to_delete_file(sender, instance, using, **kwargs):
    """
    Django signals untuk mengahapus file dari
    direktori sesudah menghapus data soal dari
    database.
    """
    file_soal = instance.file_soal.path
    import os
    os.unlink(file_soal)
    

post_save.connect(signal_to_encryption, sender=Soal)
post_delete.connect(signal_to_delete_file, sender=Soal)