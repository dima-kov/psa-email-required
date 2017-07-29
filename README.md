# An example django python social auth application 

The application shows how to create partial pipeline. Exaple is case when facebook(or any other social network) returns data without email, so we need to show a form to user where he should enter his email.

## Main parts

### `pipeline.py`

```
@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
        else:
            current_partial = kwargs.get('current_partial')
            return strategy.redirect(
                '{0}?partial_token={1}'.format(
                    reverse('app:require_email'),
                    current_partial.token
                ))

```
### `views.py`

```
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

```

## Based
Based on [python social auth examples](https://github.com/python-social-auth/social-examples), but simplified.
