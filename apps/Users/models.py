from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from uuid import uuid4


class UserTypesChoices(models.TextChoices):
    CUSTOMER = "customer"
    VENDOR = "vendor"
    NOTSET = "NotSet"


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    email_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", default="profile_pictures/default.png"
    )
    otp = models.IntegerField(default=0)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    accept_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Change this name to something unique
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",  # Change this name to something unique
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def save(self, *args, **kwargs):
        if self.user_type == "vendor":
            self.is_approved = False
        super(User, self).save()

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50, default="", blank=True)
    reset_password_expire = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=User)
def save_profile(sender: type, instance: User, created: bool, **kwargs: dict) -> None:
    if created:
        Profile.objects.get_or_create(user=instance)  # ignore the error
    else:
        # For existing users without a profile, create one
        if not hasattr(instance, "profile"):
            Profile.objects.get_or_create(user=instance)  # ignore
