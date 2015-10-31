from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # todo: add login from Class View (ok)
    url(
        # uri http://localhost:8000/
        r'^$', 
        # untk melihat list soal harus login terlebih dahulu
        login_required(
            views.SoalListView.as_view(), 
            login_url=reverse_lazy('login')
        ), 
        # nama reverse uri soal:soal-view
        name='soal-view'),
            
    url(
        # uri http://localhost:8000/soal/delete/1
        r'^soal/delete/(?P<pk>[0-9]+)/$', 
        # untuk menghapus soal harus login terlebih dahulu
        login_required(
            views.SoalDeleteView.as_view(), 
            login_url=reverse_lazy('login')
        ),
        # nama reverse uri soal:soal-delete pk=id
        name='soal-delete'),

    url(
        # uri http://localhost:8000/soal/add
        r'^soal/create/$',
        # untuk menambahkan soal harus login terlebih dahulu
        login_required(
            views.SoalCreateView.as_view(),
            login_url=reverse_lazy('login')
        ),
        # nama reverse uri soal:soal-create
        name='soal-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 