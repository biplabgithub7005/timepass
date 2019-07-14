from django import forms
from .models import Signup,UserProfile
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields ='__all__'

    email = forms.EmailField(
        label='Your Email :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email',
            }
        )
    )
    mobile = forms.CharField(
        label='Your Mobile :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Mobile',
            }
        )
    )
    password = forms.CharField(max_length=100,
                               label='Your Password :',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter Your Password',
                                   }
                               )
                               )

    username = forms.CharField(
        label='username :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Username',
            }
        )
    )


        # fields =('name')


class LoginForm(forms.Form):
    email =forms.EmailField(
        label='Your Email :',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email',
            }
        )
    )
    password =forms.CharField(max_length=100,
                              label='Your Password :',
                              widget=forms.PasswordInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Enter Your Password',
                                  }
                              )
                              )



class ProfleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','cover','fname','lname','gender','status')

    fname= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter First',
            }
        )
    )
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter First',
            }
        )
    )
    selectfields=(('', '--select Gender--'),('male', 'Male'),('female', 'Female'),)
    gender =forms.ChoiceField(choices=selectfields,
                              widget=forms.Select
                              (
                                  attrs={
                                      'class': 'form-control',
                                  }
                              )
                              )







class ChangePasswordForm(forms.Form):
    old =forms.CharField(max_length=100)
    new = forms.CharField(max_length=100)
    repeat = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old'].widget.attrs['class'] = 'form-control'
        self.fields['old'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new'].widget.attrs['class'] = 'form-control'
        self.fields['new'].widget.attrs['placeholder'] = 'New Password'
        self.fields['repeat'].widget.attrs['class'] = 'form-control'
        self.fields['repeat'].widget.attrs['placeholder'] = 'Reapeat Password'





class ResetPasswordForm(forms.Form):

    email = forms.EmailField(
        label='Enter Your Email :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email link with Project ',
            }
        )
    )


class NewPasswordForm(forms.Form):

    new = forms.CharField(max_length=100)
    repeat = forms.CharField(max_length=100)
    new.widget.attrs['class'] = 'form-control'
    repeat.widget.attrs['class'] = 'form-control'

