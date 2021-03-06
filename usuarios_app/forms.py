from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

constant =  'form-control input'

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': constant}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Primeiro Nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': constant}), label='Sobrenome')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] =  constant
        self.fields['password1'].widget.attrs['class'] =  constant
        self.fields['password2'].widget.attrs['class'] =  constant
        self.fields['first_name'].widget.attrs['class'] =  constant
        self.fields['last_name'].widget.attrs['class'] =  constant

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] =  constant
        self.fields['new_password1'].widget.attrs['class'] =  constant
        self.fields['new_password2'].widget.attrs['class'] =  constant


