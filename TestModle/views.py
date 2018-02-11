from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render_to_response
from  django.shortcuts import HttpResponse,redirect
from . import models
from . import forms
from . import wraper
import json
import os

import sys
from .public_func import common
from .public_func import HTML_helper
from django.core.files.base import ContentFile




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
    c=models.order.objects.create(petposition=1,footposition=1)
    c.save()
    print(c.get_petposition_display())
    id=models.UserInfo.objects.filter(telephone=12324).values('id')
    for i in id:
        print(i['id'])

    return render_to_response('test.html',{'a':id})

def newcase(request):
    global stat
    if request.method == 'GET':
        allusr = models.UserInfo.objects.values('id', 'name', 'telephone', 'pet_user__petname','adress','pet_user__type')
        # allusr=models.UserInfo.objects.all()
        return render_to_response('casemanagelist/newcase.html', {'da': allusr})

    elif request.method=='POST':
        start = request.POST.get('starttime')
        end = request.POST.get('endtime')
        income = request.POST.get('income')
        finishincome = request.POST.get('finishincome')
        finishincome=int(finishincome)
        telephone=request.POST.get('telephone')
        petname=request.POST.get('petname')

        orduser=models.UserInfo.objects.filter(telephone=telephone,pet_user__petname=petname).values('id','pet_user__id')
        for i in orduser:
            i=i
            if finishincome==1:
                models.order.objects.create(starttime=start, endtime=end, cashfinish=finishincome,income=income,
                                            ord_user_id=i['id'],ord_pet_id=i['pet_user__id'],status=1)
            elif finishincome==2:
                models.order.objects.create(starttime=start, endtime=end, cashfinish=finishincome, income=income,
                                            ord_user_id=i['id'], ord_pet_id=i['pet_user__id'], status=2)

        return redirect('/caselist/')
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
#
# def newuser(request):
#     if request.method == 'POST':
#         models.Pet.objects.create(photo=request.FILES['file0'])
#         return HttpResponse('OK')
#     else:
#         return render_to_response('familymanagelist/newuser.html')
def re(request):
    da=models.UserInfo.objects.all()
    allusr = models.UserInfo.objects.values('id', 'name', 'telephone', 'pet_user__petname')
    print(allusr)
    return render_to_response('casemanagelist/relatfamily.html',{'da':allusr})

# 订单列表
def caselist(request,pageid):
    ret={'resul':'','page':''}
    per_item = common.try_int(5, 5)  # 获取cookie
    count = models.order.objects.count()
    page = common.try_int(pageid, 1)
    pageobj = HTML_helper.Pageinfo(page, count, per_item)
    resul = models.order.objects.all()[pageobj.start():pageobj.end()]
    page_string = HTML_helper.pager(page, pageobj.all_page_count(),'caselist')
    ret['resul'] = resul
    ret['page'] = page_string
    if request.method=='GET':
        print(pageid)
        if pageid!='':
            models.order.objects.filter(id=int(pageid)).delete()
            return redirect('/caselist/')
        return render_to_response('casemanagelist/caselist.html',ret)
    elif request.method=='POST':
        objlist=[]
        listid=request.POST.get('caselistcaseid')
        listname=request.POST.get('caselistname')
        listtel=request.POST.get('caselisttelephone')
        if listid!='':
            filid=models.order.objects.filter(id=int(listid))
            objlist.append(filid)
        if listname!='':
            filname = models.order.objects.filter(ord_user__name=listname)
            objlist.append(filname)
        if listtel!='':
            filtel=models.order.objects.filter(ord_user__telephone=listtel)
            objlist.append(filtel)
        if 'caselsitsearch' in request.POST:
            for obj in objlist:
                print(1)
                if obj:
                    ret['obj'] = obj
                    print('no空')
                    return render_to_response('casemanagelist/caselist.html', ret)
        return render_to_response('casemanagelist/caselist.html', ret)





#待寄养家庭
def pendingcase(request,id):
    obj=models.order.objects.get(id=int(id))
    if request.method=='GET':
        return render_to_response('casemanagelist/pendingcase.html',{'obj':obj})
    else:
        finish=int(request.POST.get('finishincome'))
        cancelreasion=request.POST.get('cancelreasion')
        print(finish)
        if finish==2:
            if cancelreasion=='':
                return redirect('/caselist/')
            else:
                ord=models.order.objects.filter(id=id)
                ord.update(status=4)
                ord.update(cancelreasion=cancelreasion)
                return redirect('/caselist')
        elif finish==1:
            cc=models.order.objects.filter(id=id)
            cc.update(status=1)
            cc.update(cashfinish=finish)
            return redirect('/caselist/')
    return HttpResponse('OK')
def processingcase(request,id):
    obj=models.order.objects.get(id=int(id))
    if request.method=='GET':
        return render_to_response('casemanagelist/processingcase.html',{'obj':obj})
    else:
        petposition=request.POST.get('petposition')
        footpositon=request.POST.get('footposition')
        print(footpositon)
        models.order.objects.filter(id=id).update(petposition=petposition, footposition=footpositon)
        if ('savepro') in request.POST:
            return redirect('/caselist/')
        elif ('finishca') in request.POST:
            models.order.objects.filter(id=id).update(status=3)
            return redirect('/caselist/')

def finishcase(request,id):
    obj = models.order.objects.get(id=int(id))
    if request.method == 'GET':
        return render_to_response('casemanagelist/finishcase.html', {'obj': obj})
    else:
        return redirect('/caselist')
def cancelcase(request,id):
    obj = models.order.objects.get(id=int(id))
    if request.method == 'GET':
        return render_to_response('casemanagelist/cancelcase.html', {'obj': obj})
    else:
        return redirect('/caselist')
def familylist(request,page1):

    ret = {'resul': '', 'page': ''}
    per_item = common.try_int(5, 5)  # 获取cookie
    count = models.Pet.objects.count()
    page = common.try_int(page1, 1)
    pageobj = HTML_helper.Pageinfo(page, count, per_item)
    resul = models.Pet.objects.all()[pageobj.start():pageobj.end()]
    page_string = HTML_helper.pager(page, pageobj.all_page_count(),'familylist')
    ret['resul'] = resul
    ret['page'] = page_string
    if not os.path.exists('static/photo'):
        os.makedirs('static/photo')
    else:
        for i in resul:
            m=os.path.join('static/photo',str(i.photo))
            print(m)
    if request.method == 'GET':
        return render_to_response('familymanagelist/familylist.html', ret)
    elif request.method == 'POST':
        objlist = []
        listname = request.POST.get('familylistname')
        listtel = request.POST.get('familylisttel')
        if listname != '':
            filname = models.Pet.objects.filter(pethost__name=listname)
            objlist.append(filname)
        if listtel != '':
            filtel = models.Pet.objects.filter(pethost__telephone=listtel)
            objlist.append(filtel)
        for obj in objlist:
            if obj:
                ret['obj'] = obj
                print('no空')
                return render_to_response('familymanagelist/familylist.html', ret)
        return render_to_response('familymanagelist/familylist.html', ret)
def updatuser(request,id):
    return HttpResponse('OK')




