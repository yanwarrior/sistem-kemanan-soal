from django.shortcuts import render
from django.views.defaults import page_not_found

def custom_page_not_found(request, template_name='404.html'):
    return render(request, template_name)
