from django.urls import path
from jewelry_app.views import jewelries_detail, jewelries, jewelries_home_page


urlpatterns = [
    path("jewelries_home_page/", jewelries_home_page, name="jewelry-home-page"),
    path("jewelries_home_page/jewelries/jewelries_list",
         jewelries, name="jewelry-list"),
    path("jewelries_detail/<int:pk>/", jewelries_detail, name="jewelry-detail"),

]
