from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Primeiro Nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input'}), label='Sobrenome')
    matricula = forms.CharField(max_length=15, required=True, help_text='Obrigatório. Sua matrícula na UFRN.',label='Matrícula')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'matricula', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control input'
        self.fields['password1'].widget.attrs['class'] = 'form-control input'
        self.fields['password2'].widget.attrs['class'] = 'form-control input'
        self.fields['first_name'].widget.attrs['class'] = 'form-control input'
        self.fields['last_name'].widget.attrs['class'] = 'form-control input'
        self.fields['matricula'].widget.attrs['class'] = 'form-control input'

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control input'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control input'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control input'


