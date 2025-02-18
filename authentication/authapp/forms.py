# authapp/forms.py
from django import forms

class PasswordResetRequestForm(forms.Form):
    username_or_email = forms.CharField(max_length=254, required=True, label="Username or Email")
