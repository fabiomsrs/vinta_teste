from social_django.models import DjangoStorage

from users.models import SocialUser


class DjangoSocial(DjangoStorage):
    user = SocialUser