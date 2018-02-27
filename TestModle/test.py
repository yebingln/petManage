from . import models
def ff(request):
    t = models.order.objects.get(endtime__year=2018)
    print(t)