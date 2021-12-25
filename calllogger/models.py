from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from djangosaml2.signals import pre_user_save

# Create your models here.
from djangosaml2.signals import pre_user_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    force_password_change = models.BooleanField(default=False)
    last_password_change_date = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login_failed_at = models.DateTimeField(default=None, null=True)
    consecutive_login_failed = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'auth_user_profile'

    def __repr__(self):
        return "<UserProfile %s>" % (self.user.username)

    def __str__(self):
        return self.__repr__()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.created_at:
            self.created_at = datetime.now()
        if not self.last_password_change_date:
            self.last_password_change_date = datetime.now()
        super(UserProfile, self).save(force_insert,
                                      force_update, using, update_fields)


def update_new_saml2_user(sender, instance, attributes, user_modified, **kargs):
    instance.is_staff = True
    return True


pre_user_save.connect(update_new_saml2_user)
