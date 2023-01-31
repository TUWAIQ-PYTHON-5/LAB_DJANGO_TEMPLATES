from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("today/",views.date_pag, name="date_pag"),
    path("password/",views.random_pass_page, name="random_page"),
    path("gams/",views.Far_gmas, name="Far.gmas")
 ]