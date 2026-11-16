#Fix 5:

import logging
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

logger = logging.getLogger("security")


@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get("username", "unknown")

    ip_address = None
    if request:
        ip_address = request.META.get("REMOTE_ADDR")

    logger.warning(
        "Failed login attempt. Username: %s, IP: %s",
        username,
        ip_address
    )