from django.conf.urls import url

from app import views

urlpatterns = [
    url(
        r'^login/$',
        views.login,
        name='login'
    ),
    url(
        r'^email/$',
        views.require_email,
        name='require_email',
    ),
]
