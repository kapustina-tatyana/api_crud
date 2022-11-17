from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, MeasurementSerializer
from .models import Project, Measurement


# @api_view(http_method_names=['GET', 'POST'])
class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
