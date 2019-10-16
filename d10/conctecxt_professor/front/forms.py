from django import forms
from .models import User

class SingUpForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=30,min_length=6)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        res = User.objects.filter(username= username).exists()
        if res:
            raise forms.ValidationError("%s:用户名已经存在" % username)
        else:
            return username

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        res = User.objects.filter(telephone=telephone).exists()
        if res:
            raise forms.ValidationError("%s:手机号已存在" % telephone)
        else:
            return telephone

    def clean(self):
        cleaned_data = super(SingUpForm,self).clean()
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message="两次密码不一致")
        return cleaned_data

    class Meta:
        model = User
        fields = "__all__"

class SingInForm(forms.ModelForm):
    def get_errors(self):
        new_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.value():
            for message_dic in messages:
                for key,message in message_dic.items():
                    if key == "message":
                        new_errors.append(message)
        return new_errors

    class Meta:
        model = User
        fields = ['username','password']
        error_messages = {
            'username':{
                "min_length":"用户名不能少于6位"
            },
            'password':{
                "min_length":"密码最短不能少于6位"
            },
        }