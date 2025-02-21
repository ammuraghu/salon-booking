from django.urls import path
from .import views
urlpatterns = [
   path('',views.userindex,name="userindex"),
   path('registration',views.registration,name="registration"),
   path('regstore',views.regstore,name="regstore"),
   path('log',views.log,name="log"),
   path('publicdata',views.publicdata,name="publicdata"),
   path('userlogout',views.userlogout,name="userlogout"),
   path('viewbranch',views.viewbranch,name="viewbranch"),
   path('viewsalons/<str:branch>',views.viewsalons,name="viewsalons"),
   path('viewserv/<str:sal>',views.viewserv,name="viewserv"),
   path('contact',views.contact,name="contact"),
   path('contstore',views.contstore,name="contstore"),
   path('viewmore/<int:id>',views.viewmore,name="viewmore"),
   path('about',views.about,name="about"),
   path('booking/<int:id>',views.booking,name="booking"),
   path('bookstore/<int:id>',views.bookstore,name="bookstore"),
   path('history',views.history,name="history"),
   
]