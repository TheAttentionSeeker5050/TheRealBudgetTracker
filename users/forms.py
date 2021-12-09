"""User forms"""

from django import forms

# models
from users.models import Profile
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6, 
        max_length=100,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError("Username is already in use")
        return username

    def clean_email(self):
        """Email address must be unique."""
        email = self.cleaned_data["email"]
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError("Email is already in use")
        return email
    
    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")

        return data

    def save(self):
        """create user and profile"""
        data =  self.cleaned_data
        data.pop("password_confirmation")

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

    # class Meta:
    #     """Form settings"""
    #     model = Profile
    #     fields = ("website", "biography", "phone_number", "picture")


    