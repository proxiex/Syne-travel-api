from rest_framework import viewsets
from . import models, serializers, permissions


class FlightViewSet(viewsets.ModelViewSet):
    """
    Flight model viewSet
    """
    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()
    permission_classes = [permissions.IsSuperUserOrReadOnly, ]
