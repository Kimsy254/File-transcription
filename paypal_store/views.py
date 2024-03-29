from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal-return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal-cancel.html', args)