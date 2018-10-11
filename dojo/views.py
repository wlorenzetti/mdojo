from rest_framework import viewsets
from rest_framework.response import Response
from .models import Dojo
from .serializers import DojoSerializer


class DojoViewSet(viewsets.ModelViewSet):

    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer


