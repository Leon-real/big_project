# big_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.views import UserPasswordResetCompleteView, UserPasswordResetDoneView, UserPasswordResetConfirmView



def index(request):
    return render(request, 'index.html')

def generic(request):
    return render(request, 'generic.html')
 
def elements(request):
    return render(request, 'elements.html')

urlpatterns = [
    path('', index),
    path("admin/", admin.site.urls),
    path('account/', include('account.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('client/', include('client.urls')),
    path('post/', include('post.urls')),
    path('index.html', index, name='index'),
    path('generic.html', generic, name='generic'),
    path('elements.html', elements, name='elements'),
    # path('password_reset_done/', UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
