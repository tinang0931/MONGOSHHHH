from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anna/', include('anna.urls')),  # Include your app's URLs here
]
