from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegistrUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'phone', 'country', 'avatar', ]

    def __init__(self, *args, **kwargs):
        super(RegistrUserForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields.get(field).widget.attrs.update({
                'class': 'form-control',
                # 'placeholder': f'Введите {field}'
            })
