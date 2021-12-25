from datetime import datetime
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile


class LoginRequiredMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if any(url in request.path for url in settings.LOGIN_BYPASS_BASE_URLS):
            return None
        if request.user.is_anonymous:
            path = request.path
            if settings.STATIC_URL not in path and path != settings.LOGIN_URL or not path:
                return HttpResponsePermanentRedirect(settings.LOGIN_URL)
        else:
            profile, created = UserProfile.objects.get_or_create(
                user=request.user)
            profile.last_password_change_date = profile.last_password_change_date
            profile.last_active_at = datetime.now()
            profile.save()
