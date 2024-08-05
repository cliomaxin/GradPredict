from django.contrib import admin
from django.urls import path, include
from . import views

#if Static does not load import these modules
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("view", views.view, name="view"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if Static Files does not load add the above line of code imediately after the bracket for url patterns