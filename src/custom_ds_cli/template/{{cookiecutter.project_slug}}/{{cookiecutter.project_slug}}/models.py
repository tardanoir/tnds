"""Models for {{ cookiecutter.project_name }} project."""
from django.db import models


class MLModel(models.Model):
    """Machine Learning model metadata."""
    
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Model performance metrics
    accuracy = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    recall = models.FloatField(null=True, blank=True)
    f1_score = models.FloatField(null=True, blank=True)
    
    # Model parameters and artifacts
    parameters = models.JSONField(default=dict)
    artifact_path = models.CharField(max_length=255, blank=True)
    
    class Meta:
        """Model metadata."""
        
        ordering = ['-created_at']
    
    def __str__(self):
        """String representation of the model."""
        return f"{self.name} v{self.version}" 