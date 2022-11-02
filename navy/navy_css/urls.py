from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('report',views.report,name="report"),
    re_path(r'^(?P<color>[\S\n\t\v\s]+)\/index\.css', views.css, name="css")
]