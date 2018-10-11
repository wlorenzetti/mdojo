from rest_framework.serializers import ModelSerializer
from .models import Dojo


class DojoSerializer(ModelSerializer):

    class Meta:
        model = Dojo
        fields = '__all__'