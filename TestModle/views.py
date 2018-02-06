from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render_to_response
from  django.shortcuts import HttpResponse,redirect
from . import models
from . import forms
from . import wraper
import json

# Create your views here.

def login(request):
    loginform=forms.login()
    ret={'form':None,'err':""}
    ret['form'] = loginform
    if request.method=='POST':
        checkform=forms.login(request.POST)

        if checkform.is_valid():
            u=request.POST.get('telephone')
            p=request.POST.get('password')
            if models.Account.objects.filter(telephone=u,password=p):
                uu=models.Account.objects.filter(telephone=u).values('username')
                for i in uu:
                    ni=i['username']
                request.session['is_login']={'ni':ni}
                return redirect('/')
            else:
                ret['form']=checkform
                ret['err']='用户名或密码错误'
                return render_to_response('login.html',ret)
    return render_to_response('login.html',ret)

def register(request):
    obj=forms.register()
    if request.method=='POST':
        checkform=forms.register(request.POST)
        if checkform.is_valid():
            data=checkform.cleaned_data
            models.Account.objects.create(username=data['username'],password=data['password'])
            return render_to_response('login.html')
        else:
            return HttpResponse('失败')
    return render_to_response('register.html',{'form':obj})

# @wraper.Loginwraper
def default(request):
    request.session['is_login']={'ni':1111}
    username=request.session['is_login']
    return render_to_response('master/default.html',{'user':username['ni']})
# @wraper.Loginwraper
def home2(request):
    return render_to_response('Home2.html')
# @wraper.Loginwraper
def test(request):
    cc=models.position
    c=models.position.objects.create(petposition=1,footposition=1)
    c.save()
    print(c.get_petposition_display())
    id=models.UserInfo.objects.filter(telephone=12324).values('id')
    for i in id:
        print(i['id'])

    return render_to_response('test.html',{'a':cc})

def newcase(request):
    if request.method == 'GET':
        allusr = models.UserInfo.objects.values('id', 'name', 'telephone', 'pet_user__petname','adress','pet_user__type')
        return render_to_response('casemanagelist/newcase.html', {'da': allusr})
    elif request.method=='POST':
        start = request.POST.get('starttime')
        end = request.POST.get('endtime')
        income = request.POST.get('income')
        finishincome = request.POST.get('finishincome')
        telephone=request.POST.get('telephone')
        petname=request.POST.get('petname')
        orduser=models.UserInfo.objects.filter(telephone=telephone,pet_user__petname=petname).values('id','pet_user__id')
        for i in orduser:
            i=i
            models.order.objects.create(starttime=start, endtime=end, finishincome=finishincome,ord_user_id=i['id'],ord_pet_id=i['pet_user__id'])
        return redirect('/caselist/')


def processingcase(request):
    return render_to_response('casemanagelist/processingcase.html')
def caselist(request):
    c=models.order.objects.all().values('id','starttime','endtime')
    print(c)
    return render_to_response('casemanagelist/caselist.html')
def newuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        telephone=request.POST.get('telephone')
        address=request.POST.get('address')
        petname=request.POST.getlist('petname')
        pettype=request.POST.getlist('pettype')
        newuserpetlike=request.POST.getlist('newuserpetlike')
        file0=request.POST.getlist('file0')
        models.UserInfo.objects.create(name=username,telephone=telephone,adress=address)
        id=models.UserInfo.objects.filter(telephone=telephone).values('id')
        for i in id:
            host_id=i['id']
        biglist=zip(petname,pettype,newuserpetlike,file0)
        for i in biglist:
            models.Pet.objects.create(petname=i[0], type=i[1], like=i[2], photo=i[3],pethost_id=host_id)
        return HttpResponse('ok')
    return render_to_response('familymanagelist/newuser.html')

def re(request):
    da=models.UserInfo.objects.all()
    allusr = models.UserInfo.objects.values('id', 'name', 'telephone', 'pet_user__petname')
    print(allusr)
    return render_to_response('casemanagelist/relatfamily.html',{'da':allusr})