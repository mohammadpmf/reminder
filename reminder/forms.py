from django import forms

from .models import Reminder


class ReminderFormToSHow(forms.Form):
    active = forms.BooleanField(disabled=True)
    sms = forms.BooleanField(disabled=True)
    email = forms.BooleanField(disabled=True)
    telegram = forms.BooleanField(disabled=True)
    whatsapp = forms.BooleanField(disabled=True)
    notification = forms.BooleanField(disabled=True)
    eta = forms.BooleanField(disabled=True)
    bale = forms.BooleanField(disabled=True)


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ["title", "period", "active", "email", "telegram"]

    title = forms.CharField(max_length=64, label="عنوان یادآوری")
    period = forms.TypedChoiceField(
        choices=Reminder.PERIOD_CHOICES,
        label="دوره چرخش یادآوری",
        widget=forms.Select(attrs={"style": "height: 40px;"}),
    )
    active = forms.BooleanField(
        required=False,
        initial=True,
        help_text="در صورت غیر فعال کردن یک یادآوری، پیامی از طرف سایت برای شما ارسال نخواهد شد.",
        label="فعال بودن این یادآوری",
    )
    email = forms.BooleanField(
        required=False,
        initial=True,
        help_text="جهت دریافت پیام از طریق ایمیل، باید از قسمت تنظیمات سایت آدرس ایمیل معتبر خود را وارد کنید.",
        label="ارسال ایمیل",
    )
    telegram = forms.BooleanField(
        required=False,
        initial=True,
        help_text="جهت دریافت پیغام از طریق تلگرام، باید از قسمت تنظیمات سایت، chat_id تلگرامی خود را اضافه کنید و یک پیغام از اکانت مورد نظر برای ربات تلگرامی با آی دی @sbede_bot ارسال کنید تا ربات تلگرامی توانایی ارسال پیغام برای شما را داشته باشد.",
        label="ارسال پیام در تلگرام",
    )
    # sms = forms.BooleanField(disabled=True, help_text='در حال حاضر فعال نیست', label='اس ام اس')
    # whatsapp = forms.BooleanField(disabled=True, help_text='در حال حاضر فعال نیست', label='واتساپ')
    # notification = forms.BooleanField(disabled=True, help_text='در حال حاضر فعال نیست', label='نوتیفیکیشن')
    # eta = forms.BooleanField(disabled=True, help_text='در حال حاضر فعال نیست', label='ایتا')
    # bale = forms.BooleanField(disabled=True, help_text='در حال حاضر فعال نیست', label='بله')
