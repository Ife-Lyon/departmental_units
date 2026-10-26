from django.db import models

class DepartmentalUnit(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="e.g., Retail Banking")
    code = models.CharField(max_length=50, unique=True, blank=True, null=True, help_text="e.g., RET")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide from FormBuilder dropdown")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name