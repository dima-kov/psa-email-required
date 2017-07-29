from django.shortcuts import render

from social_django.utils import load_strategy


def login(request):
    return render(request, 'login.html')


def require_email(request):
    """Email required page"""
    strategy = load_strategy()
    partial_token = request.GET.get('partial_token')
    partial = strategy.partial_load(partial_token)
    return render(
        request, 'require_email.html', {
            'email_required': True,
            'partial_backend_name': partial.backend,
            'partial_token': partial_token
        }
    )
