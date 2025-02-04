"""Views for {{ cookiecutter.project_name }} project."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MLModel
from .serializers import MLModelSerializer


class MLModelViewSet(viewsets.ModelViewSet):
    """ViewSet for MLModel."""

    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer

    @action(detail=True, methods=["get"])
    def metrics(self, request, pk=None):
        """Get model metrics."""
        model = self.get_object()
        metrics = {
            "accuracy": model.accuracy,
            "precision": model.precision,
            "recall": model.recall,
            "f1_score": model.f1_score,
        }
        return Response(metrics)

    @action(detail=True, methods=["get"])
    def parameters(self, request, pk=None):
        """Get model parameters."""
        model = self.get_object()
        return Response(model.parameters)
