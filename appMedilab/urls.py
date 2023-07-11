from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMedilab.views import home

urlpatterns = [
    path('home/', home),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)