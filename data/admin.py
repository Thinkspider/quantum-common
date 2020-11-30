# Register your models here.
from django.contrib import admin

from .models import AgencyDiversityCategory
from .models import Ethnicity
from .models import Naics


@admin.register(Naics)
class NaicsAdmin(admin.ModelAdmin):
    list_display = ('code', 'standard_employee_count', 'standard_revenue')


@admin.register(AgencyDiversityCategory)
class AgencyDiversityCategoryAdmin(admin.ModelAdmin):
    list_display = ('agency', 'regions', 'diversity_categories')


@admin.register(Ethnicity)
class EthnicityAdmin(admin.ModelAdmin):
    list_display = ('ethnicity', 'regions')
