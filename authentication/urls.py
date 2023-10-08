from django.contrib import admin
from django.urls import include, path

from update import settings
from . import views
from django.conf.urls.static import static

# Add all file diroctery in side the view and templet filename as acdording to the views. py
# Create a templets filefor html 
# Create a static file for img,css,js



urlpatterns = [
   path('',views.home,name="home"),
   path('signup',views.signup,name="signup"),
   path('signout',views.signout,name="signout"),
   path('signin',views.signin,name="signin"),
   path('about',views.about,name="about"),
   path('contact',views.contact,name="contact"),
   path('design',views.design,name="design"),
   path('preatics',views.preatics,name="preatics"),
   path('userdetails',views.userdetails,name="userdetails"),
   path('regst',views.regst,name="regst"),
   path('u_dash',views.u_dash,name="u_dash"),
   path('u_info',views.u_info,name="u_info"),
   path('u_project',views.u_project,name="u_project"),
   path('u_document',views.u_document,name="u_document"),
   path('u_setting',views.u_setting,name="u_setting"),
   path('u_help',views.u_help,name="u_help"),
   #path('',views.,name=""),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
