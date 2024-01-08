from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from .models import ProfilePic
class NewUserForm(UserCreationForm):
    

    password1 = forms.CharField(label="password",widget=forms.PasswordInput(
                                    attrs={"class":"mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300",
                                           "id":"signup-password",
                                            "placeholder":"password"}))
    password2 = forms.CharField(label="password",widget=forms.PasswordInput(
                                    attrs={"class":"mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300",
                                           "id":"signup-password",
                                            "placeholder":"Confirm-password"}))

    class Meta:
        model = User
        fields = ("username",'email','password1','password2')
        widgets = {'username':forms.TextInput(attrs={'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}),
                   'email':forms.EmailInput(attrs={'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}),
                   }
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update()
    def save(self, commit: bool = ...) -> Any:
        user = super(NewUserForm,self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit :
            user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300', 
               'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300',
            'placeholder': 'password',
            'id': 'signin-password',
        }
))
class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any) -> None:
        my_html_class = 'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class':my_html_class ,
            'placeholder': 'Enter old password',
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': my_html_class,
            'placeholder': 'Enter new password',
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': my_html_class,
            'placeholder': 'Confirm new password',
        })
class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ImageUploadForm(forms.ModelForm):
    
    class Meta:
        model = ProfilePic
        fields = ['image','user']