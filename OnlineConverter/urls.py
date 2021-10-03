from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('any_non_standard_path/admin/', admin.site.urls),  # Admin panel path
    path('', include('main.urls')),                         # Main Path
    path('api/v1/', include('api.urls'))                    # API view
]


