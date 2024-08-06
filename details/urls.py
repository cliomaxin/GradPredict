from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

#if Static does not load import these modules
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("studentDetailscapture/", views.studentDetailscapture, name="studentDetailscapture"),
    path('success/', views.success, name='success'),
    #if seperate html pages
    # path('signin/', views.signin, name="signin"),
    # path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"), 
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name='password_reset_complete'), 
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if Static Files does not load add the above line of code imediately after the bracket for url patterns