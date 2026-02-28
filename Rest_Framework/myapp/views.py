
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import employee

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')

        if username:
            return employee.objects.filter(username=username)

        return employee.objects.all()
