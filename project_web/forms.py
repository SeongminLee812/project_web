from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyMemberForm(UserCreationForm):
    """
    UserCreationForm 에는 기본적으로 'username', 'password1', 'password2' field가 내장되어 있다.
    password1 : 비밀번호
    password2 : 비밀번호 확인
    """
    email = forms.EmailField()
    name = forms.CharField()

    class Meta:
        model = User # User 모델 객체 => admin페이지에서 보이는
        fields = ('username', 'password1', 'password2', 'email', 'name')