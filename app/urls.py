from django.urls import path
from . import views
urlpatterns = [
    path('',views.testview),
    path('input',views.input),
    path('output/<int:id>',views.output),
    path('getques',views.getques),
    path('getdata',views.getdata),
    path('getdata2', views.getdata2),
    path('login',views.login)


]
