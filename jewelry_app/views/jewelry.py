from re import template
from urllib import request
from django.shortcuts import render
from django.views.decorators.http import require_GET
from jewelry_app.models import Jewelry


@require_GET
def jewelries_home_page(request):
    return render(request=request, template_name="jewelry_app/jewelries_home_page.html", context=None)


@require_GET
def jewelries(request):
    queryset = Jewelry.objects.all()
    content = {
        "jewelries": queryset
    }
    return render(request=request, template_name="jewelry_app/jewelries_list.html", context=content)


@require_GET
def jewelries_detail(request, pk=None):
    queryset = Jewelry.objects.get(pk=pk)
    content = {
        "jewelries_detail": queryset
    }
    return render(request=request, template_name="jewelry_app/jewelries_detail.html", context=content)
