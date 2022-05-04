from django.urls import path
from .import views
urlpatterns = [
    path('', views.homefun,name="home"),
    path('login/', views.loginfun,name="login"),
    path('login/forgetpass/', views.forgetpasfun,name="forgetpass"),
    path('login/forgetpass/resetpass/', views.resetpasfun,name="resetpass"),
    path('adminhome/', views.adminhomefun,name="adminhome"),
    path('signup/', views.signupfun,name="signup1"),
]
