# Create your views here.
from django.db.models import F
from django.db.models import Func
from django.http.response import JsonResponse
from rest_framework import views
from rest_framework import viewsets

from .models import AgencyDiversityCategory
from .models import Ethnicity
from .models import Naics
from .serializers import AgencyDiversityCategorySerializer
from .serializers import EthnicitySerializer
from .serializers import NaicsSerializer


class NaicsViewset(viewsets.ModelViewSet):
    serializer_class = NaicsSerializer
    queryset = Naics.objects.all()


class AgencyDiversityCategoryViewset(viewsets.ModelViewSet):
    serializer_class = AgencyDiversityCategorySerializer
    queryset = AgencyDiversityCategory.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('region'):
            queryset = queryset.filter(regions__contains=self.request.GET.getlist('region'))
        if self.request.GET.get('diversity_category'):
            queryset = queryset.filter(diveristy_categories__contains=self.request.GET.getlist('diversity_category'))
        return queryset


class EthnicityViewset(viewsets.ModelViewSet):
    serializer_class = EthnicitySerializer
    queryset = Ethnicity.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('region'):
            queryset = queryset.filter(regions__contains=self.request.GET.getlist('region'))
        return queryset


class DiversityCategoryListView(views.View):
    queryset = AgencyDiversityCategory.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.queryset
        if request.GET.get('region'):
            queryset = queryset.filter(regions__contains=request.GET.getlist('region'))
        diversity_categories = queryset.annotate(
            diversity_categories_elements=Func(F('diversity_categories'), function='unnest')
        ).values_list(
            'diversity_categories_elements', flat=True
        ).order_by('diversity_categories_elements').distinct()
        return JsonResponse(data=list(diversity_categories), status=200, safe=False)
