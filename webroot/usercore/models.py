from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager, CustomSubscriptionidManager, CustomSubscriptionManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    if len(str(value))!=10:
        raise ValidationError(
            _("%(value)s is not a phone number"),
            params={"value": value},
        )
    else:
        return value
    
def validate_gstin(value):
    if len(str(value))!=15:
        raise ValidationError(
            _("%(value)s is not a gstin number"),
            params={"value": value},
        )
    else:
        return value
    
class User(AbstractUser):
    last_name = models.CharField(max_length=100, verbose_name='Last Name', null=True, blank=True)
    gstin_Number = models.CharField(max_length=15, verbose_name='GSTIN Number', validators=[validate_gstin], null=True, blank=True)
    businessName = models.CharField(max_length=40, verbose_name='Business Name')
    businessid=models.ForeignKey(to='businessid', on_delete=models.PROTECT, default=0)
    phone_contact = models.IntegerField(verbose_name="Phone Number(+91 only)", validators=[validate_phone], help_text="Enter your Phone Number.")
    department = models.ForeignKey(to='departments', on_delete=models.PROTECT, default='', null=True, blank=True)
    department_access = models.BooleanField(default=False)
    login_time_from = models.TimeField(null=True)
    login_time_to = models.TimeField(null=True)
    admin_access = models.BooleanField(default=False)
    sub_admin = models.BooleanField(default=False, null=True, blank=True)
    insurance_read_access = models.BooleanField(default=False, null=True, blank=True)
    workshop_read_access = models.BooleanField(default=False, null=True, blank=True)
    stock_read_access = models.BooleanField(default=False, null=True, blank=True)
    insurance_add_access = models.BooleanField(default=False, null=True, blank=True)
    workshop_add_access = models.BooleanField(default=False, null=True, blank=True)
    stock_add_access = models.BooleanField(default=False, null=True, blank=True)
    insurance_update_access = models.BooleanField(default=False, null=True, blank=True)
    workshop_update_access = models.BooleanField(default=False, null=True, blank=True)
    stock_update_access = models.BooleanField(default=False, null=True, blank=True)
    insurance_delete_access = models.BooleanField(default=False, null=True, blank=True)
    workshop_delete_access = models.BooleanField(default=False, null=True, blank=True)
    stock_delete_access = models.BooleanField(default=False, null=True, blank=True)
    subscription = models.ForeignKey(to='subscriptionsid', on_delete=models.PROTECT, default='0000')

    # objects = models.Manager()
    objects_manager = CustomUserManager()

    # class Meta:
    #     permissions=[
    #         (
    #             "is_admin","checks if the user is admin or not."
    #         ),(
    #             "is_subscribed","checks if the subscription is valid."
    #         ),(
    #             "is_sub-admin","checks if the user is sub-admin."
    #         ),(
    #             "can_department_access","checks if the user can access department data."
    #         ),
            # (
            #     "can_insurance_read","checks if the user can read insurance data."
            # ),(
            #     "can_stock_read","checks if the user can read stock data."
            # ),(
            #     "can_workshop_read","checks if the user can read workshop data."
            # ),(
            #     "can_insurance_write","checks if the user can write insurance data."
            # ),(
            #     "can_stock_write","checks if the user can write stock data."
            # ),(
            #     "can_workshop_write","checks if the user can write workshop data."
            # ),(
            #     "can_insurance_update","checks if the user can update insurance data."
            # ),(
            #     "can_stock_update","checks if the user can update stock data."
            # ),(
            #     "can_workshop_update","checks if the user can update workshop data."
            # ),(
            #     "can_insurance_delete","checks if the user can delete insurance data."
            # ),(
            #     "can_stock_delete","checks if the user can delete stock data."
            # ),(
            #     "can_workshop_delete","checks if the user can delete workshop data."
            # ),
        # ]

class businessid(models.Model):
    objects = models.Manager()
    
class departments(models.Model):
    # id=models.IntegerField(auto_created=True, editable=False, primary_key=True, unique=True, blank=FALSE, default=)
    name=models.CharField(max_length=20, primary_key=True)
    objects = models.Manager()


class subscriptionsid(models.Model):
    objects=CustomSubscriptionidManager()

class subscriptions(models.Model):
    subscriptionid = models.OneToOneField(to=subscriptionsid, on_delete=models.PROTECT)
    businessid = models.ForeignKey(to='businessid', on_delete=models.PROTECT, default='')
    timestamp = models.DateTimeField(auto_now=True, editable=False)
    start_date = models.DateTimeField(verbose_name='Start_Date')
    end_date = models.DateTimeField()
    is_valid = models.BooleanField(default=False)
    amount = models.FloatField(editable = False, blank=False, null=False)
    duration = models.DurationField(editable = False, null = False, blank=False)
    Discount = models.FloatField(editable=False, blank=False)
    transaction_id = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=10, choices={'pass':'pass', 'fail':'fail'}, default='fail')
    objects = CustomSubscriptionManager()

    # class Meta:
    #     permissions = [
    #         (
    #             "is_admin","checks if the user is an admin."
    #         ),]


#"""admin in this context is a user who is the owner of the business,
#  under which other employees work"""

