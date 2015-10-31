from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import user_passes_test

from soal.admin import admin_site_tu


# create forbidden page
# ---------------------
# login page automatic redirect after user login.
# login page can't accessing user after login.
# this lamdba function to checking anonymous user,
# if user is anonymous, login page can access by user.
login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
    # localhost/admin
    url(r'^admin/', include(admin.site.urls)),
    
    # localhost/tu
    url(r'tu/', include(admin_site_tu.urls)),
    
    # localhost
    url(r'', include('soal.urls', namespace='soal')),
    
    # localhost/login
    url(
        r'^login/', 
        login_forbidden(login), 
        kwargs = {
            'template_name':'soal/login.html',
        }, name='login'
    ),
    
    # localhost/logout
    url(r'^logout/', 'django.contrib.auth.views.logout',
        kwargs={
            'next_page':reverse_lazy('login')
        }, name='logout')
        
] 


handler404 = 'errorhandling.views.custom_page_not_found'
