"""orderservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orderapp.views import order_service
from orderapp.views import change_status_wait, change_status_send
from orderapp.views import change_status_reject, change_status_recieved
from orderapp.views import create_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orderservice/', order_service),
    path('orderservice/create-order/', create_order),
    path('orderservice/wait/<int:pk>/', change_status_wait),
    path('orderservice/send/<int:pk>/', change_status_send),
    path('orderservice/rjct/<int:pk>/', change_status_reject),
    path('orderservice/rcvd/<int:pk>/', change_status_recieved)
]
