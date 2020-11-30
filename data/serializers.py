from rest_framework.serializers import ModelSerializer

from .models import AgencyDiversityCategory
from .models import Ethnicity
from .models import Naics


class NaicsSerializer(ModelSerializer):

    class Meta:
        model = Naics
        fields = '__all__'


class AgencyDiversityCategorySerializer(ModelSerializer):

    class Meta:
        model = AgencyDiversityCategory
        fields = '__all__'


class EthnicitySerializer(ModelSerializer):

    class Meta:
        model = Ethnicity
        fields = '__all__'
