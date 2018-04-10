from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from app_name import models
from django.forms import fields
from django import forms
# model 与 form 分离
class UserInfoForm(forms.Form):
    username = fields.CharField(max_length=32,label='用户名')
    email = fields.EmailField(label='邮箱')
    user_type = fields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption'),
        label='国籍'
    )
    def __init__(self,*args,**kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')

def index(request):

    if request.method == 'GET':
        obj = UserInfoForm()
        return render(request, 'modelForm.html', {'obj':obj})
    elif request.method == 'POST':
        obj = UserInfoForm(request.POST)
        s = obj.is_valid()
        obj.errors
        # print('s: ',s)
        # print('obj.cleaned_data: ',obj.cleaned_data)
        if s:
            dic = obj.cleaned_data;
            dic['user_type_id'] = obj.cleaned_data['user_type']
            del dic['user_type']
            # print('dic: ', dic)
            models.UserInfo.objects.create(**dic)
            # models.UserInfo.objects.filter(id=1).update(**dic)
        return render(request,'modelForm.html',{'obj':obj})


