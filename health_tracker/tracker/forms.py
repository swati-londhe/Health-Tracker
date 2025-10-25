from django import forms
from .models import HealthLog

class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        fields = ['steps', 'calories', 'water_intake', 'sleep_hours']
