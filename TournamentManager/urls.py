from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('reg/', include('registration.urls')),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls"))
]