from django.contrib.auth.forms import UserCreationForm
from .models import MyUserClass

class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUserClass
        fields = ("first_name","last_name","email", "password1", "password2")