from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from app02 import models
def login(request):
    return HttpResponse('login')

def upload(request):
    return render(request,'upload.html')
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# 去除csrf
@csrf_exempt
def upload_file(request):

    username = request.GET.get('username')
    fafafa = request.FILES.get('fafafa')
    print('fafafa : ',fafafa)
    import os
    img_path = os.path.join('static/images',fafafa.name)
    with open(img_path,'wb') as f:
        for item in fafafa.chunks():
            f.write(item)
    ret = {'code':True,'data':img_path}
    import json
    return HttpResponse(json.dumps(ret))


# model 相关代码
def app(request):
    if request.method == 'GET':
        app_list = models.Appliction.objects.all()
        host_list = models.Host.objects.all()
        return render(request,'app.html',{'app_list': app_list,'host_list': host_list})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name,host_list)

        obj = models.Appliction.objects.create(name=app_name)
        obj.r.add(*host_list)

        return redirect('/user/app')



