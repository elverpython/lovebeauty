"""
URL configuration for lovebeauty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('worker/worker_detail/<int:pk>/', worker_detail, name='worker-detail'),
    path('worker/worker_edit/<int:pk>/', worker_edit, name='worker-edit'),
    path('list-class/', WorkerView.as_view(), name='worker-list-class'),
    path('add-worker/', worker_add_form),
    path('create-brand/', create_brand, name='create-brand'),
    path('brands-list/', BrandsView.as_view(), name='brand-list-class'),
    path('brand/brand_detail/<int:pk>/', brand_detail, name='brand-detail'),
    path('brand/brand-edit/<int:pk>/', brand_edit, name='brand-edit'),
    path('create-client/', create_client, name='create-client'),
    path('clients-list/', ClientsView.as_view(), name='client-list-class'),
    path('client/client_detail/<int:pk>/', client_detail, name='client-detail'),
    path('client/client-edit/<int:pk>/', client_edit, name='client-edit'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

