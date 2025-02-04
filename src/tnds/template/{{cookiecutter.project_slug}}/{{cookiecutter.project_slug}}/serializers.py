"""Serializers for {{ cookiecutter.project_name }} project."""

from rest_framework import serializers

from .models import MLModel


class MLModelSerializer(serializers.ModelSerializer):
    """Serializer for MLModel."""

    class Meta:
        """Serializer metadata."""

        model = MLModel
        fields = [
            "id",
            "name",
            "version",
            "description",
            "created_at",
            "updated_at",
            "accuracy",
            "precision",
            "recall",
            "f1_score",
            "parameters",
            "artifact_path",
        ]
        read_only_fields = ["created_at", "updated_at"]
