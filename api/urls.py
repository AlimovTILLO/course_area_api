from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('cities', CityViewSet)
router.register('schools', SchoolViewSet)
router.register('courses', CourseViewSet)


api_urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
]
