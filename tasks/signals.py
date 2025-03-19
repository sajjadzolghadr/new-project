from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task

@receiver(post_save, sender=Task)
def send_task_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Task Created',
            f'Your task "{instance.title}" has been created.',
            'from@example.com',
            [instance.user.email],
            fail_silently=False,
        )
