import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.contents.models import Contact
from .models import TelegramAdmin


TOKEN = '7257801118:AAE45vLTXWfmJE4XXeMjJstYL7YA5SurEDY'

def send_message_url(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, json=payload)
    return response.json()


def send_telegram_message(message):
    bot_admins = TelegramAdmin.objects.values_list('chat_id', flat=True) 
    if not bot_admins:
        return
    
    for chat_id in bot_admins:
        try:
            send_message_url(TOKEN, chat_id, message)
        except:
            pass

    return 'Success - send message.'


@receiver(post_save, sender=Contact)
def contact_notification(sender, instance, created, **kwargs):
    if created:
        message = (
            f"📮Новая заявка!\n\n"
            f"Id: {instance.id}\n"
            f"Имя: {instance.full_name}\n"
            f"Телефон: {instance.phone_number}\n"
            f"Город: {instance.city}\n"
            f"Автомобиль: {instance.auto}\n"
            f"Дата начала: {instance.date_start}\n"
            f"Дата окончания: {instance.date_end}\n"
        )
        send_telegram_message(message)