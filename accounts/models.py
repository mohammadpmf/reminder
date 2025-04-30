from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="Phone number must be exactly 11 digits.",
                code="invalid_phone_number",
            ),
        ],
        unique=True,
        blank=False,
        null=False,
    )
    telegram_chat_id = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        verbose_name="چت آی دی تلگرام",
    )
