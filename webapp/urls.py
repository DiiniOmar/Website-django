
from django.conf.urls.static import static
from portfolio import settings
from django.contrib import admin
from django.urls import path, include
from webapp import views


urlpatterns = [
    
      path('', views.home, name="index"),
      path('contact/', views.contactView, name='contact'),
      path('upload/', views.Upload_document, name="upload_document"),
      path('download/<int:resume_id>/', views.download_pdf, name='download_pdf'),
      path('download_redirects/', views.download_redirect, name='download_redirects')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
