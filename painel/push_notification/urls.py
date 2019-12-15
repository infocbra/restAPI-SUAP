from django.urls import path

from . import views

urlpatterns = [
    path('save_information', views.save_info, name='save_webpush_info'),
    # Service worker need to be loaded from same domain
    path('service-worker.js', views.ServiceWorkerView.as_view(), name='service_worker')
]
