#coding='utf-8f'
from django.shortcuts import redirect

def Loginwraper(function):
    def islogin(request):
        sessioncheck=request.session.get('is_login')
        print(sessioncheck)
        if sessioncheck:
            return function(request)

        else:
            return redirect('/login/')
    return islogin

