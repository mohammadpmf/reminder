from django.db import models
from django.contrib.auth import get_user_model


class Reminder(models.Model):
    ONE_TIME = "one time"
    EVERY_YEAR = "every year"
    EVERY_MONTH = "every month"
    EVERY_30_DAYS = "every 30 days"
    EVERY_28_DAYS = "every 28 days"
    EVERY_14_DAYS = "every 14 days"
    EVERY_WEEK = "every week"
    EVERY_3_DAYS = "every 3 days"
    EVERY_2_DAYS = "every 2 days"
    EVERY_DAY = "every day"
    EVERY_12_HOURS = "every 12 hours"
    EVERY_8_HOURS = "every 8 hours"
    EVERY_6_HOURS = "every 6 hours"
    EVERY_4_HOURS = "every 4 hours"
    EVERY_180_DAYS = "every 180 days"
    EVERY_120_DAYS = "every 120 days"
    EVERY_90_DAYS = "every 90 days"
    EVERY_60_DAYS = "every 60 days"
    EVERY_21_DAYS = "every 21 days"
    EVERY_15_DAYS = "every 15 days"
    EVERY_10_DAYS = "every 10 days"
    EVERY_5_DAYS = "every 5 days"
    EVERY_4_DAYS = "every 4 days"
    EVERY_10_YEARS = "every 10 years"
    EVERY_7_YEARS = "every 7 years"
    EVERY_5_YEARS = "every 5 years"
    EVERY_4_YEARS = "every 4 years"
    EVERY_3_YEARS = "every 3 years"
    EVERY_2_YEARS = "every 2 years"

    PERIOD_CHOICES = (
        (ONE_TIME, "یک بار"),
        (EVERY_YEAR, "هر سال"),
        (EVERY_MONTH, "هر ماه"),
        (EVERY_30_DAYS, "هر ۳۰ روز"),
        (EVERY_28_DAYS, "هر ۲۸ روز"),
        (EVERY_14_DAYS, "هر ۱۴ روز"),
        (EVERY_WEEK, "هر هفته"),
        (EVERY_3_DAYS, "هر ۳ روز"),
        (EVERY_2_DAYS, "هر ۲ روز"),
        (EVERY_DAY, "هر روز"),
        (EVERY_12_HOURS, "هر ۱۲ ساعت"),
        (EVERY_8_HOURS, "هر ۸ ساعت"),
        (EVERY_6_HOURS, "هر ۶ ساعت"),
        (EVERY_4_HOURS, "هر ۴ ساعت"),
        (EVERY_180_DAYS, "هر ۱۸۰ روز"),
        (EVERY_120_DAYS, "هر ۱۲۰ روز"),
        (EVERY_90_DAYS, "هر ۹۰ روز"),
        (EVERY_60_DAYS, "هر ۶۰ روز"),
        (EVERY_21_DAYS, "هر ۲۱ روز"),
        (EVERY_15_DAYS, "هر ۱۵ روز"),
        (EVERY_10_DAYS, "هر ۱۰ روز"),
        (EVERY_5_DAYS, "هر ۵ روز"),
        (EVERY_4_DAYS, "هر ۴ روز"),
        (EVERY_10_YEARS, "هر ۱۰ سال"),
        (EVERY_7_YEARS, "هر ۷ سال"),
        (EVERY_5_YEARS, "هر ۵ سال"),
        (EVERY_4_YEARS, "هر ۴ سال"),
        (EVERY_3_YEARS, "هر ۳ سال"),
        (EVERY_2_YEARS, "هر ۲ سال"),
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="reminders"
    )
    title = models.CharField(max_length=64)
    start_datetime = models.DateTimeField()
    period = models.CharField(max_length=64, choices=PERIOD_CHOICES)
    active = models.BooleanField(default=True, verbose_name="فعال")
    email = models.BooleanField(default=True, verbose_name="ایمیل")
    telegram = models.BooleanField(default=True, verbose_name="تلگرام")
    sms = models.BooleanField(default=False, verbose_name="اس ام اس")
    notification = models.BooleanField(default=False, verbose_name="نوتیفیکیشن")
    whatsapp = models.BooleanField(default=False, verbose_name="واتساپ")
    eta = models.BooleanField(default=False, verbose_name="ایتا")
    bale = models.BooleanField(default=False, verbose_name="بله")

    def __str__(self):
        return self.title
