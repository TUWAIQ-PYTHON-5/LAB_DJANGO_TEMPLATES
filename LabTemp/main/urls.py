from . import views
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.todate, name='todate'),
    path('generatpwd/',views.generat_password,name='generat_password'),
    path('favgame/',views.fav_game,name='fav_game'),


]