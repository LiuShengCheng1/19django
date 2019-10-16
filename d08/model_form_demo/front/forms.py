from django import forms
from .models import Article,User


class AddArticleForm(forms.ModelForm):
    def clean_word_num(self):
        word_num = self.cleaned_data.get('word_num')
        if word_num > 100:
            raise forms.ValidationError('总词数不能超过100')
        return word_num
    class Meta:
        model = Article
        fields = '__all__'  # 使用model中所有的字段
        # exclude = ['word_num'] 排除指定的字段
        error_messages ={
            'word_num':{
                'required':'请传入word_num参数',
                'invalid':'请传入正确的word_num参数'
            },
            'title':{
                'max_length':'title最大不能超过100个字符',
            },
            'price':{
                'max_value':'文章价不能超过100圆'
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')



    class Meta:
        model = User
        exclude = ['password']