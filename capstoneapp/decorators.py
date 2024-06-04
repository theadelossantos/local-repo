from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def mdrrmc_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user_type == 'mdrrmc':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access Denied")
    return _wrapped_view


def barangay_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user_type == 'barangay':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access Denied")
    return _wrapped_view