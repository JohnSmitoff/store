from django import forms
from .models import Animal
from .models import Owner
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
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    age = forms.IntegerField(
        required=True,
        min_value=1,
        validators=[
            RegexValidator(
                r"^[1-9]\d*$",
                message="The age must be positive number bigger then zero",
            )
        ],
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    breed = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    image_url = forms.URLField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}), required=True
    )
    kind = forms.ChoiceField(
        choices=choices, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Animal
        fields = ("name", "age", "breed", "description", "image_url", "kind")


class OwnerForm(forms.ModelForm):
    choices = list(Owner.OWNER_SEX)
    first_name = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                r"^[A-Z][a-z]+$", message="First name must start with capital letter"
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                r"^[A-Z][a-z]+$", message="Last name must start with capital letter"
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    image_url = forms.URLField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    owner_sex = forms.ChoiceField(
        choices=choices, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Owner
        fields = ("first_name", "last_name", "owner_sex", "image_url")
