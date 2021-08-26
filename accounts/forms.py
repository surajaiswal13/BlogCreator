# from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from BlogCreatorWeb.logger import get_log

logger = get_log('blog')

class UserForm(UserCreationForm):
    """
    This class is used for creation of user registration form
    """

    def __init__(self,*args,**kwargs):
        """
        __init__ method is used for Initialization of UserForm class
        """

        try:
            super().__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Display Name'
            self.fields['email'].widget.attrs["placeholder"] = "example@mail.com"
            self.fields['password1'].widget.attrs["placeholder"] = "Password"
            self.fields['password2'].widget.attrs["placeholder"] = "Password Confirmation"
            self.fields['email'].widget.attrs["placeholder"] = "example@mail.com"
            self.fields['username'].label = ""
            self.fields['email'].label = ""
            self.fields['password1'].label = ""
            self.fields['password2'].label = ""
        except Exception as e:
            logger.error('The error in UserForm - __init__ method is :'+str(e))
            print(e)

    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()

class UserLoginForm(AuthenticationForm):
    """
    This class is used for creation of user login form
    """

    def __init__(self,*args,**kwargs):

        """
        __init__ method is used for Initialization of UserLoginForm class
        """

        try:
            super().__init__(*args, **kwargs)
            self.fields['username'].label = ""
            self.fields['password'].label = ""
            self.fields['username'].widget.attrs["placeholder"] = "Username"
            self.fields['password'].widget.attrs["placeholder"] = "Password"
        except Exception as e:
            logger.error('The error in UserLoginForm - __init__ method is :'+str(e))
            print(e)