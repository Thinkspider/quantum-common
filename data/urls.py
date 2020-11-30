from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AgencyDiversityCategoryViewset
from .views import DiversityCategoryListView
from .views import EthnicityViewset
from .views import NaicsViewset

router = DefaultRouter()
router.register(r'naics', NaicsViewset, basename='user')
router.register(r'agencydiversitycategory', AgencyDiversityCategoryViewset, basename='user')
router.register(r'ethnicity', EthnicityViewset, basename='user')

urlpatterns = [
    path(r'diversitycategory/', DiversityCategoryListView.as_view()),
    path('', include(router.urls)),
]
