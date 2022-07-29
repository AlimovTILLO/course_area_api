from django.urls import path, include

api_urlpatterns = [
    path('/', include('rest_framework.urls')),
    path('accounts/', include('rest_registration.api.urls')),
]
