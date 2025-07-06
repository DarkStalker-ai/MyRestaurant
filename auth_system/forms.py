from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Чоловік'),
        ('F', 'Жінка'),
        ('O', 'Інше'),
    ]
    email = forms.EmailField(required=True, label='Електронна пошта')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)           

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', "gender")
        labels = {
            'username': "Ім'я користувача",
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        gender = self.cleaned_data['gender']

        if gender == 'M':
            avatar_path = 'static/img/default_avatar.jpg'
        elif gender == 'F':
            avatar_path = 'static/img/default_avatar.jpg'
        else:
            avatar_path = 'static/img/default_avatar.jpg'
        
        profile = UserProfile(
            user=user,
            gender=gender,
            avatar=avatar_path)
        if commit:
            profile.save()
        
        return user

    # Ця штука переводить текст форми і забирає підказки так шо не трогайте
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Підтвердження пароля"

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'gender', 'bio')