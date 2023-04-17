from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name="index"),
    path('baja_cliente/',views.baja_cliente,name='baja_cliente'),
    path('alta_cliente/',views.alta_cliente,name='alta_cliente'),
    path('alta_usuar io/',views.alta_usuario,name='alta_usuario'),
    path('baja_usuario/',views.baja_usuario,name='baja_usuario'),
    path('login/',views.login,name='login'),
    
    

]