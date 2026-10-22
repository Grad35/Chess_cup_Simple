from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[path("",views.home,name="home"),path("register/",views.signup,name="signup"),path("login/",auth_views.LoginView.as_view(template_name="tournaments/login.html"),name="login"),path("logout/",auth_views.LogoutView.as_view(),name="logout"),path("cabinet/",views.dashboard,name="dashboard"),path("apply/<int:tournament_id>/",views.apply_tournament,name="apply")]
