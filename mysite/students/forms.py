

from django import forms
from students.models import Student
# create elements inside the form
class StudentForm(forms.Form):
    # provide fields create html
    name=forms.CharField(max_length=120)
    email=forms.EmailField(max_length=120)
    grade = forms.IntegerField(min_value=0, max_value=100)
    image = forms.ImageField(required=False)


    # define validation rule for email
    def clean_email(self):
        email = self.cleaned_data['email']
        email_found = Student.objects.filter(email=email).exists()
        if email_found:
            raise forms.ValidationError("Email already registered before")
        return email


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")

        return name


