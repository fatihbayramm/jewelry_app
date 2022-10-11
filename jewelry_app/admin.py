from django.contrib import admin
from jewelry_app.models import Jewelry


@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "jewelry_kind"]


#admin.site.register(Jewelry, JewelryAdmin)
