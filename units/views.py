from rest_framework import generics
from rest_framework.response import Response
from .models import DepartmentalUnit
from .serializers import DepartmentalUnitSerializer

class DepartmentalUnitListView(generics.ListAPIView):
    """
    API endpoint that fetch all active Departmental Units.
    """
    queryset = DepartmentalUnit.objects.filter(is_active=True)
    serializer_class = DepartmentalUnitSerializer
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "success": True,
            "message": "Departmental units retrieved successfully.",
            "total": queryset.count(),
            "data": serializer.data
        })