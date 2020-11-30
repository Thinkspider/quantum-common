from django.contrib.postgres.fields import ArrayField
from django.db import models


class Naics(models.Model):
    code = models.IntegerField()
    descriptions = ArrayField(models.TextField())
    standard_employee_count = models.IntegerField(null=True, blank=True)
    standard_revenue = models.IntegerField(null=True, blank=True)


class AgencyDiversityCategory(models.Model):
    agency = models.CharField(max_length=128)
    regions = ArrayField(models.TextField())
    diversity_categories = ArrayField(models.TextField())


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=128)
    regions = ArrayField(models.TextField())
