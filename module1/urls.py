
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name="print_to_console"),
    path('p/',print1,name='print1'),
    path('otp/',randomcall1,name="randomcall1"),
    path('otplogic/',randomcall,name="randomcall"),
    path('get_date/',get_date,name='get_date'),
    path('get_date1/',get_date1,name='get_date1'),
    path('register/',registerlogin,name='registerlogin'),
    path('registerlogin/',registerloginfunction,name='registerloginfunction'),
    path('pie/',pie_chart,name='pie'),
    path('piechart/',piechart,name='piechart'),
    path('carrent/',Car,name='carrent'),
    path('temp/',weatherpagecall,name='weatherpagecall'),
    path('Temparture/',weatherlogic,name='weatherlogic'),
    path('logout/',logout,name='logout'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signup1/', signup1, name='signup1'),
    path('login1/', login1, name='login1'),
    path('feedback/', feedback, name='feedback'),
    path('feedbackfunction/', feedbackfunction, name='feedbackfunction'),
]

