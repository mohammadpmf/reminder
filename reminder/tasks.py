# your_app/tasks.py
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import timedelta
from django.utils import timezone
from .models import Reminder
import pytz

logger = get_task_logger(__name__)

YEARS_PERIOD_DICT = {
    Reminder.EVERY_YEAR: 1,
    Reminder.EVERY_10_YEARS: 10,
    Reminder.EVERY_7_YEARS: 7,
    Reminder.EVERY_5_YEARS: 5,
    Reminder.EVERY_4_YEARS: 4,
    Reminder.EVERY_3_YEARS: 3,
    Reminder.EVERY_2_YEARS: 2,
}
PERIOD_DICT = {
    Reminder.EVERY_30_DAYS: 2592000,
    Reminder.EVERY_28_DAYS: 2419200,
    Reminder.EVERY_14_DAYS: 1209600,
    Reminder.EVERY_WEEK: 604800,
    Reminder.EVERY_3_DAYS: 259200,
    Reminder.EVERY_2_DAYS: 172800,
    Reminder.EVERY_DAY: 86400,
    Reminder.EVERY_12_HOURS: 43200,
    Reminder.EVERY_8_HOURS: 28800,
    Reminder.EVERY_6_HOURS: 21600,
    Reminder.EVERY_4_HOURS: 14400,
    Reminder.EVERY_180_DAYS: 15552000,
    Reminder.EVERY_120_DAYS: 10368000,
    Reminder.EVERY_90_DAYS: 7776000,
    Reminder.EVERY_60_DAYS: 5184000,
    Reminder.EVERY_21_DAYS: 1814400,
    Reminder.EVERY_15_DAYS: 1296000,
    Reminder.EVERY_10_DAYS: 864000,
    Reminder.EVERY_5_DAYS: 432000,
    Reminder.EVERY_4_DAYS: 345600,
}


def should_send(reminder: Reminder):
    now = timezone.now()
    time_diff = now - reminder.start_datetime
    time_diff = int(time_diff.total_seconds())
    period = reminder.period
    if period in PERIOD_DICT:
        result = time_diff % PERIOD_DICT.get(period)
        if result<60:
            return True
        return False
    else:
        reminder_year = reminder.start_datetime.year
        reminder_month = reminder.start_datetime.month
        reminder_day = reminder.start_datetime.day
        reminder_hour = reminder.start_datetime.hour
        reminder_minute = reminder.start_datetime.minute
        if period in YEARS_PERIOD_DICT:
            if any(
                [
                    reminder_minute != now.minute,
                    reminder_hour != now.hour,
                    reminder_day != now.day,
                    reminder_month != now.month,
                ]
            ):
                return False
            year_diff = now.year - reminder_year
            result = year_diff % YEARS_PERIOD_DICT.get(reminder.period)
            if result==0:
                return True
            return False
        elif period == Reminder.EVERY_MONTH:
            if any(
                [
                    reminder_minute != now.minute,
                    reminder_hour != now.hour,
                    reminder_day != now.day,
                ]
            ):
                return False
            return True
        elif period == Reminder.ONE_TIME:
            if time_diff<60:
                return True
            return False


@shared_task(bind=True)
def check_and_send_reminders(self):
    now = timezone.now()
    reminders = Reminder.objects.filter(
        active=True, start_datetime__lte=now
    ).select_related("user")
    print(reminders)
    for reminder in reminders:
        print(f"{now=}")
        print(f"{reminder.title=}")
        print(f"{reminder.start_datetime=}")
        print(f"{reminder.period=}")
        if should_send(reminder):
            send_reminder.delay(reminder)


@shared_task(bind=True)
def send_reminder(self, reminder:Reminder):
    if reminder.email:
        send_email.delay(reminder)
    if reminder.telegram:
        send_telegram.delay(reminder)

        
@shared_task(bind=True, max_retries=3)
def send_email(self, reminder:Reminder):
    1


@shared_task(bind=True, max_retries=3)
def send_telegram(self, reminder:Reminder):
    1