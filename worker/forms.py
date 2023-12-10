from django import forms
from .models import Worker


class WorkerEditForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'name',
            'specialization',
            'salary',
            'is_working',

        ]

class WorkerAddForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'name',
            'specialization',
            'salary',
            'is_working',

        ]