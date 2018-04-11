from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from app_name import models
from django.forms import fields
from django import forms
from django.forms import widgets as Fwidgets

#modelform
class UserInfoModelForm(forms.ModelForm):
    is_rmb = fields.CharField(widget=Fwidgets.CheckboxInput())

    class Meta:
        model = models.UserInfo
        # 包含全部字段
        fields = '__all__'
        # 包含哪些字段
        # fields = ['username','email']
        # 去除哪些字段
        exclude = ['u2g']
        labels = {
            'username':'用户名',
            'email':'邮箱'
        }
        help_texts = {
            'username':'....'
        }
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class': 'c1'})

        }
        error_messages = {
            '__all__': {

            },
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误'
            }
        }
        field_classes = {
            # 'email': fields.URLField
        }
        localized_fields = ('ctime',)

    def clean_username(self):
        old = self.cleaned_data['username']
        return old

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
        # self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')

def user_list(request):
    li = models.UserInfo.objects.all().select_related('user_type')
    return render(request,'user_list.html',{'li': li})

def user_edit(request, nid):
    if request.method == 'GET':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})

def indexMF(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request,'modelForm.html',{'obj': obj})
    elif request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            instance = obj.save(False)
            instance.save()
            obj.save_m2m();
        return render(request,'modelForm.html',{'obj': obj})


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
            # 外键
            dic['user_type_id'] = obj.cleaned_data['user_type']
            del dic['user_type']
            # print('dic: ', dic)
            models.UserInfo.objects.create(**dic)
            # models.UserInfo.objects.filter(id=1).update(**dic)
        return render(request,'modelForm.html',{'obj':obj})


