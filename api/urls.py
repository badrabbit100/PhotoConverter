from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('photos/', views.PhotoList.as_view(), name='photos'),
    path('delete_all/', views.delete_all, name='delete_all'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
