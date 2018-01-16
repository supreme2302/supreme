from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class RegistrationForm(forms.Form):
    login = forms.CharField(min_length=5,label='login')
    email = forms.EmailField(label='emal')
    username = forms.CharField(label='username')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='repeat password')
    #avatar = forms.ImageField(label='avatar')

class SettingForm(forms.Form):
    login = forms.CharField(min_length=5,label='login')
    email = forms.EmailField(label='emal')
    username = forms.CharField(label='username')

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(max_length=510,widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.CharField(max_length=100)

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))


