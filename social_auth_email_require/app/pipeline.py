from social_core.pipeline.partial import partial
from django.urls import reverse


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
