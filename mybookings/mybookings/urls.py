from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Change 'mybookings.urls' to 'myapp.urls'
    path('api/', include('myapp.urls')),
]