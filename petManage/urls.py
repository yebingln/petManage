"""petManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TestModle import views
from petManage import settings
from django.conf.urls.static import static
from petManage.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^$', views.default),
    url(r'^test/$', views.test),
    url(r'^home2/$', views.home2),
    url(r'^newcase/$', views.newcase),
    url(r'^processingcase/$', views.processingcase),
    url(r'^caselist/(\d*)', views.caselist),
    url(r'^newuser/', views.newuser),
    url(r'^updateuser/(\d*)', views.updatuser),
    url(r'^re/$', views.re),
    url(r'^casestatus/2/(\d*)$', views.pendingcase),
    url(r'^casestatus/1/(\d*)$', views.processingcase),
    url(r'^casestatus/3/(\d*)$', views.finishcase),
    url(r'^casestatus/4/(\d*)$', views.cancelcase),
    url(r'^familylist/(\d*)', views.familylist),
    url(r'^newpayout/', views.newpayout),
    url(r'^paylist/', views.paylist),
    url(r'^incomelist/', views.incomelist),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
