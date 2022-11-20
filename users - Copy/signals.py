
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = Profile()
        profile.user = user
        profile.save()

post_save.connect(create_profile, sender=User)
