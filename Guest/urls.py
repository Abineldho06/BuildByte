from django.urls import path,include
from Guest import views
app_name='Guest'

urlpatterns = [
    path('Registration/',views.Registration,name="Registration"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),

    path('login/',views.login,name="login"),
    path('',views.index,name="index"),
]
