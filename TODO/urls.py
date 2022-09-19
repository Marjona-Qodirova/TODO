
from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('rejalar/', rejalar),
    path('register/', register),
    path('bajarilmaganlar/',  bajarilmagan_rejalar),
    path('', loginView, name='login'),
    path('logout/', logoutView),
    path('reja_ochir/<int:pk>/' ,reja_ochir),
    path('rejalar_edit/<int:pk>/' ,reja_edit),


]
