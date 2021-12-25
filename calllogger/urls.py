from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="calllogpage"),
    path("calllogpage/", views.calllogpage, name="loadcalllogpage"),
    path("calllogpage/calllogdownloader/", views.downloader, name="calllogdownloader")
    
]