from rest_framework import viewsets
from . import models, serializers, permissions


class FlightViewSet(viewsets.ModelViewSet):
    """
    Flight model viewSet
    """
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    permission_classes = [permissions.IsSuperUserOrReadOnly]
