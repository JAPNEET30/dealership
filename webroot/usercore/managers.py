from multiprocessing.managers import BaseManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, first_name, username, password, last_name, gstin_Number, businessid, email,
                     is_active, admin_access, businessName, subscription, phone_contact):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set."))
        if not username:
            raise ValueError(_("The Username Must be set."))
        if not password:
            raise ValueError(_("The Password must be set."))
        
        user = self.model(first_name=first_name,
                     username =username,
                     last_name = last_name,
                     gstin_Number = gstin_Number,
                     businessid = businessid,
                     email = email,
                     is_active =is_active,
                     admin_access = admin_access,
                     businessName = businessName,
                     subscription = subscription,
                     phone_contact = phone_contact)
        user.set_password(password)
        user.save()
        return user
    
    # def create_subscription(self, businessid, )

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, username, password, **extra_fields)

class CustomSubscriptionidManager(BaseManager):
    # def create():
    pass

class CustomSubscriptionManager(BaseManager):
    # def create():
    pass