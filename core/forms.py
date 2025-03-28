from django import forms
from .models import Review, Appointment, Package

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'review']

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all active packages and create choices
        packages = Package.objects.all()
        package_choices = [(p.name, f"{p.name} (Rs. {p.cost})") for p in packages]
        self.fields['package'].widget = forms.Select(choices=[('', 'Select a Package')] + package_choices)

    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'age', 'gender', 'package', 'preferred_date', 'message']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'package': forms.Select(attrs={'class': 'form-control'}),
        }