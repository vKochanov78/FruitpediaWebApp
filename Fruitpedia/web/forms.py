from django import forms
from .models import Profile, Fruit


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password'
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password'
            })
        }


class FruitCreationForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }