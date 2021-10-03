from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.photo_upload, name='photo_upload'),
    path('delete/<str:pk>/', views.photo_delete, name='photo_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
