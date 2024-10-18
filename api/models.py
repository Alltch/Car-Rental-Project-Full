from django.db import models


class TelegramAdmin(models.Model):
    chat_id = models.BigIntegerField(
        unique=True, 
        verbose_name="Telegram ID", 
        help_text="Уникальный ID администратора в Telegram"
    )
    first_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Имя", 
        help_text="Имя администратора"
    )
    last_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Фамилия", 
        help_text="Фамилия администратора"
    )
    username = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Имя пользователя", 
        help_text="Имя пользователя администратора в Telegram"
    )
    language_code = models.CharField(
        max_length=10, 
        null=True, 
        blank=True, 
        verbose_name="Код языка", 
        help_text="Код языка по умолчанию, установленный у администратора"
    )
    is_bot = models.BooleanField(
        default=False, 
        null=True, 
        blank=True, 
        verbose_name="Является ботом", 
        help_text="Указывает, является ли этот пользователь ботом"
    )
    is_premium = models.BooleanField(
        default=False, 
        null=True, 
        blank=True, 
        verbose_name="Премиум пользователь", 
        help_text="Отмечает, есть ли у администратора премиум-статус"
    )
    cteated_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления", 
        help_text="Дата и время последнего изменения записи"
    )

    def get_fullname(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return self.username
        elif self.first_name:
            return self.first_name
        else:
            return "Unknown"

    def str(self):
        return f"Admin: {self.get_fullname()} [{self.chat_id}]"

    class Meta:
        verbose_name = "Telegram администратор"
        verbose_name_plural = "Telegram администраторы"
        ordering = ["-cteated_at"]