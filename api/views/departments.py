from rest_framework import viewsets

from api.models import Departments
from api.serializers import DepartmentSerializer


class DepartmentsViewset(viewsets.ModelViewSet):

    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer