from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from jewelry_app.models import Jewelry
from django.db.models import Q


class RoleView(LoginRequiredMixin, View):
    def get(self, request):

        user = Jewelry.objects.filter(Q(author=request.user))

        context = {
            "user": user,
        }

        return render(request=request, template_name="registration/login.html", context=context)
