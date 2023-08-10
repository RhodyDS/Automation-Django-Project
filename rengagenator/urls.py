
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('customers/',include('customers.urls')),
    path('',include('dashboard.urls')),
    path('admin/', admin.site.urls),

]
