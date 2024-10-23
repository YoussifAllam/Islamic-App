from django.db import models
from apps.Users.models import User

# 1. 👇 Add the following line


class NotificationsModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    subject = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}"

    def mark_as_read(self):
        self.is_read = True
        self.save()
