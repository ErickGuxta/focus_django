from django import forms

#importando User padrão Django e validações
from django.contrib.auth.models import User

#para o lado do user público
class RegisterForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'email'   : forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if commit:
            user.save()
        return user

#para o lado do admim
class UserForm(forms.ModelForm):

    #metaclasse
    class Meta:

        model = User
        fields = [ 'username', 'email', 'is_active', 'is_superuser', 'password']

        widgets = {
            'username'    : forms.TextInput( attrs={'class': 'form-control','autocomplete': 'off'}),
            'email'       : forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),    
            'password'    : forms.PasswordInput( attrs={'class': 'form-control', 'autocomplete': 'off'},),

            'is_active'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),   

        }

    #def para salvar senha
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)  # Salva a senha corretamente, com hash(eu acho)
        if commit:
            user.save()
        return user
