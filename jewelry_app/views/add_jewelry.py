from re import template
from jewelry_app.forms import AddJewelry
from django.shortcuts import render
from django.http import HttpResponseRedirect


def add_jewelry_form(request):
    if request.method == "POST":
        form = AddJewelry(request.POST)
    else:
        form = AddJewelry()
    return render(request=request, template_name="jewelry_app/jewelry_form.html", context={"form": form})
