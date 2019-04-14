from django import forms
from .models import Animal
from django.core.validators import RegexValidator


class AnimalForm(forms.ModelForm):
    choices = list(Animal.KIND_CHOICES)
    name = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                r"^[A-Z][a-z]+$", message="Name must start with capital letter"
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    age = forms.IntegerField(required=True ,widget=forms.TextInput(attrs={"class": "form-control"}))
    breed = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    image_url = forms.URLField(required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), required=True)
    kind = forms.ChoiceField(choices=choices,widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Animal
        fields = ("name", "age", "breed", "description", "image_url", "kind")
