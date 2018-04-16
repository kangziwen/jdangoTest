from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
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



