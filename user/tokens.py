""" Token generator for verifications """

import random
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenFactory(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return(
            text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)
        )

class OTPFactory():
    def get_otp(self):
        return random.randint(100000, 999999)

email_auth_token = TokenFactory()
pass_reset_token = TokenFactory()
email_auth_otp = OTPFactory()
