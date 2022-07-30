from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import viewsets, mixins

from .models import Category, SubCategory, School, Course, City
from .serializers import CategorySerializer, SubCategorySerializer, CitySerializer, CourseSerializer, SchoolSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class SchoolViewSet(ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class CourseViewSet(ReadOnlyModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Course.objects.filter(isActive=True)
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['rating',]
    search_fields = ['title']