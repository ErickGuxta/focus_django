from django import forms
from django.contrib.auth import get_user_model

#importando User padrão Django e validações
# from django.contrib.auth.models import User

User = get_user_model()

class UserForm(forms.ModelForm):

    #metaclasse
    class Meta:

        model = User
        fields = [ 'username', 'email', 'nome', 'is_active', 'is_staff', 'is_superuser', 'password']

        widgets = {
            'username'    : forms.TextInput( attrs={'class': 'form-control','autocomplete': 'off'}),
            'email'       : forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),    
            'nome'        : forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'password'    : forms.PasswordInput( attrs={'class': 'form-control', 'autocomplete': 'off'},),

            'is_active'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
            'is_staff'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),   

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['password'].required = False

    #def para salvar senha
    def save(self, commit=True):
        old_password = None
        if self.instance and self.instance.pk:
            old_password = User.objects.only("password").get(pk=self.instance.pk).password

        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)  # Salva a senha corretamente, com hash(eu acho)
        elif old_password:
            user.password = old_password

        if commit:
            user.save()
        return user
