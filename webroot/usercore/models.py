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
    business_address = models.CharField(verbose_name = 'business_address', max_length=200, null = False, blank=False, default='Jagdalpur')
    subscription = models.ForeignKey(to='subscriptionsid', on_delete=models.PROTECT, default='0000')
    objects_manager = CustomUserManager()

    class Meta:
        permissions=[
            ("is_admin","checks if the user is admin or not."),
            ]

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

class EmployeeUser(AbstractUser):
    
    businessid=models.ForeignKey(to=businessid, on_delete=models.PROTECT, default='0001', related_name='business_id')
    employeeid = models.IntegerField(verbose_name='Employee ID', null=False, blank = False)
    phone_contact = models.IntegerField(verbose_name="Phone Number(+91 only)", validators=[validate_phone], help_text="Enter your Phone Number.")
    address = models.CharField(max_length = 200, verbose_name='Address', null=True, blank=True)
    login_time_to = models.TimeField(null=True)
    created_on = models.TimeField(null=False, auto_created=True)

    class Meta:
        default_permissions = ()
        permissions = [
            ("employee_is_admin", "Is the admin"),
        ("add_package", "Can add a package"),
        ("update_package", "Can update a package"),
        ("delete_package", "Can delete a package"),
        ("view_package", "Can view packages"),
        ('all_perm_packages',"all permissions packages"),

        ("add_team", "Can add a team"),
        ("update_team", "Can update a team"),
        ("delete_team", "Can delete a team"),
        ("view_team", "Can view teams"),
        ("add_members", "Can add members to a team"),
        ("deactivate_members", "Can deactivate team members"),
        ("activate_members", "Can activate team members"),
        ('all_perm_team',"all permissions teams"),

        ("view_network_package", "Can view network packages"),
        ("approve_network_package", "Can approve network packages"),

        ("create_insurance_track", "Can create an insurance track"),
        ("update_insurance_track", "Can update an insurance track"),
        ("delete_insurance_track", "Can delete an insurance track"),
        ("view_insurance_track", "Can view insurance tracks"),
        ('all_perm_insurance_track',"all permissions insurance track"),

        ("create_item", "Can create an item"),
        ("update_item", "Can update an item"),
        ("delete_item", "Can delete an item"),
        ("view_items", "Can view items"),
        ("add_stock", "Can add stock"),
        ("delete_stock", "Can delete stock"),
        ("update_stock", "Can update stock"),
        ("view_stock", "Can view stock"),
        ('all_perm_stock',"all permissions stock"),

        ("add_task", "Can add a task"),
        ("update_task", "Can update a task"),
        ("delete_task", "Can delete a task"),
        ("view_task", "Can view tasks"),
        ('all_perm_workshop',"all permissions workshop"),

        ("ask_service", "Can ask for a service"),
        ("start_service", "Can start a service"),
        ("stop_service", "Can stop a service"),
        ("view_service", "Can view services"),
        ("monitor_service", "Can monitor services"),
        ('all_perm_services',"all permissions service"),

        ("view_feedback", "Can view feedback"),
        ("get_feedback", "Can retrieve feedback details"), # Renamed for clarity
        ("mark_feedback", "Can mark feedback"),
        ('all_crm_permissions',"all permissions crm"),
        ]

    USERNAME_FIELD = str(businessid)+str(employeeid)
    REQUIRED_FIELDS = ['businessID', ]

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='employee groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        related_name="employeeuser_set_groups", # Unique related_name
        related_query_name="employeeuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='employee permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="employeeuser_set_perms", # Unique related_name
        related_query_name="employeeuser",
    )