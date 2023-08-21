from django import forms
from core.models import Recipe, CookingCategory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import User  

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        max_length=100
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=100
    )

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe 
        fields = ['title', 'description', 'image', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id': 'image'}))
    category = forms.ModelChoiceField(queryset=Recipe.objects.all(), empty_label=None)
