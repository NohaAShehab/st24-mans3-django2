from django import forms
from tracks.models import Track
class TrackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        found = Track.objects.filter(name=name).exists()
        if found:
            raise forms.ValidationError('This name is already taken.')
        return name



