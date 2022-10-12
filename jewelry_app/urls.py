from django.urls import path
from jewelry_app.views import jewelries_detail, jewelries, jewelries_home_page
from jewelry_app.views.add_jewelry import add_jewelry_form


urlpatterns = [
    path("jewelries_home_page/", jewelries_home_page, name="jewelry-home-page"),
    path("jewelries_home_page/jewelries/jewelries_list",
         jewelries, name="jewelry-list"),
    path("jewelries_detail/<int:pk>/", jewelries_detail, name="jewelry-detail"),
    path("form/", add_jewelry_form,  name="add-jewelry-form"),

]
