from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb',None) == '1':
                request.session.set_expiry(10)
            return redirect('/index/')
        else:
            return render(request,'login.html')

from django.views.decorators.csrf import csrf_protect
@csrf_protect
def index(request):

    if request.session.get('is_login',None):
        return render(request,'index.html',{'username':request.session['username']})
    else:
        return HttpResponse('gunduzi')


def logout(request):
    request.session.clear()
    return redirect('/login')

