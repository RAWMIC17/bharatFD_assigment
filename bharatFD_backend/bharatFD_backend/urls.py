from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line
    path('faq/', include('faq.urls')),  # Your existing path
]
