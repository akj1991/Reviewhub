from django.urls import path
from .import views
urlpatterns = [
    path('', views.homefun,name="home"),
    path('login/', views.loginfun,name="login"),
    path('login/forgetpass/', views.forgetpasfun,name="forgetpass"),
    path('login/forgetpass/resetpass/', views.resetpasfun,name="resetpass"),
    path('dashboard/', views.adminhomefun,name="adminhome"),
    path('signup/', views.signupfun,name="signup1"),
    path('dashboard/creator/', views.creatorfun,name="creator"),
    path('creator/delete/<int:id>',views.deletefun,name="delete"),
    path('creator/update/<int:id>',views.updatefun,name="update"),
    path('dashboard/viewers/', views.viewerfun,name="viewers"),
    path('dashboard/reports/', views.reportsfun,name="reports"),
    path('dashboard/requests/', views.requestsfun,name="request"),
    path('dashboard/settings/', views.settingsfun,name="settings"),
    path('dashboard/uploaded-videos-list/', views.uploadvideofun,name="upvideos"),
    path('login/creatorlogin/', views.creloginfun,name="creatorlogin"),
    path('login/viewerlogin/', views.viewerloginfun,name="viewerlogin"),
    path('login/creatorlogin/creatorforgotpass/', views.creatorforpassfun,name="creatorforgetpass"),
    path('login/creatorlogin/creatorforgotpass/creatorresetpassword/', views.creatorrestpassfun,name="creatorresetpass"),
    path('login/viewerlogin/viewerforgotpass/', views.viewerforpassfun,name="viewerforgotpass"),
    path('login/viewerlogin/viewerforgotpass/viewerresetpassword/', views.viewerrestpassfun,name="viewerresetpass"),
]
