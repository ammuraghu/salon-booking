from django.urls import path
from .import views
urlpatterns = [
    path('adminindex',views.adminindex,name="adminindex"),
    path('branches',views.branches,name="branches"),
    path('branchtable',views.branchtable,name="branchtable"),
    path('branchstore',views.branchstore,name="branchstore"),
    path('branchedit/<int:id>',views.branchedit,name="branchedit"),
    path('breditstore/<int:id>',views.breditstore,name="breditstore"),
    path('brdelete/<int:id>',views.brdelete,name="brdelete"),
    path('saloon',views.saloon,name="saloon"),
    path('saltable',views.saltable,name="saltable"),
    path('salstore',views.salstore,name="salstore"),
    path('saledit/<int:id>',views.saledit,name="saledit"),
    path('saloostore/<int:id>',views.saloostore,name="saloostore"),
    path('saldelete/<int:id>',views.saldelete,name="saldelete"),
    path('service',views.service,name="service"),
    path('servtable',views.servtable,name="servtable"),
    path('servstore',views.servstore,name="servstore"),
    path('servedit/<int:id>',views.servedit,name="servedit"),
    path('serupdate/<int:id>',views.serupdate,name="serupdate"),
    path('servdelete/<int:id>',views.servdelete,name="servdelete"),
    path('viewreg',views.viewreg,name="viewreg"),
    path('viewcont',views.viewcont,name="viewcont"),
    path('viewbook',views.viewbook,name="viewbook"),
    path('approvebooking/<int:id>',views.approvebooking,name="approvebooking"),
    path('decline/<int:id>',views.decline,name="decline")
]