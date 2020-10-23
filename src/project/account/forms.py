from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )

    password = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 100,
        widget = forms.PasswordInput(
            attrs={
                'class': 'input100'
            }
        )
    )
    
    